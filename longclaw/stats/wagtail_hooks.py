import datetime

from django.template.loader import render_to_string

from wagtail import hooks
from wagtail.admin.ui.components import Component

from longclaw.configuration.models import Configuration
from longclaw.orders.models import Order
from longclaw.stats import stats
from longclaw.utils import ProductVariant, maybe_get_product_model


class LongclawSiteSummary(Component):
    order = 100

    def outstanding_orders(self, parent_context):
        orders = Order.objects.filter(status=Order.SUBMITTED)
        return {
            "total": orders.count(),
            "label": "Outstanding Orders",
            "url": "/admin/orders/order/",
        }

    def product_count(self, parent_context):
        product_model = maybe_get_product_model()
        if product_model:
            count = product_model.objects.all().count()
        else:
            count = ProductVariant.objects.all().count()
        return {
            "total": count,
            "label": "Products",
        }

    def sales_count(self, parent_context):
        settings = Configuration.for_request(parent_context["request"])
        sales = stats.sales_for_time_period(*stats.current_month())
        return {
            "total": f"{settings.currency_html_code}{sum(order.total for order in sales)}",
            "label": "In sales this month",
            "url": "/admin/orders/order/",
        }

    def render_html(self, parent_context):
        return render_to_string(
            "stats/site_summary.html",
            {
                "outstanding_orders": self.outstanding_orders(parent_context),
                "product_count": self.product_count(parent_context),
                "sales_count": self.sales_count(parent_context),
            },
        )


@hooks.register("construct_homepage_panels")
def site_summary_panel(request, panels):
    panels.append(LongclawSiteSummary())


class LongclawStatsPanel(Component):
    order = 110
    template_name = "stats/stats_panel.html"

    def get_context(self):
        month_start, month_end = stats.current_month()
        daily_sales = stats.daily_sales(month_start, month_end)
        labels = [
            (month_start + datetime.timedelta(days=x)).strftime("%Y-%m-%d")
            for x in range(0, datetime.datetime.now().day)
        ]
        daily_income = [0] * len(labels)
        for k, order_group in daily_sales:
            i = labels.index(k)
            daily_income[i] = float(sum(order.total for order in order_group))

        popular_products = stats.sales_by_product(month_start, month_end)[:5]
        return {
            "daily_income": daily_income,
            "labels": labels,
            "product_labels": list(popular_products.values_list("title", flat=True)),
            "sales_volume": list(popular_products.values_list("quantity", flat=True)),
        }


@hooks.register("construct_homepage_panels")
def statistics_panel(request, panels):
    panels.append(LongclawStatsPanel())
