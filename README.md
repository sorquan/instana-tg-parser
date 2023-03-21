# Local run:
### Export required environment variables:
```
export TG_TOKEN='<bot_token>'
export TG_CHAT='<chat_id>'
```
### Build:
```
docker build -t instana-webhook .
```
### Run:
```
docker run -p 5000:5000 -e TG_CHAT -e TG_TOKEN instana-webhook
```
