# Developer Notes

This is a temporary document to chart the further development of the package to support the latest versions of Django and Wagtail.

## In this work

- Add this document to the project
- the minimum python should be 3.8 for the moment. Thats likely to be bumped to 3.9 in the near future.
- For tests to run you need to build the fontend static assets.

### Build Frontend

```bash
cd longclaw/client
nvm use
npm install
npm run build
```
