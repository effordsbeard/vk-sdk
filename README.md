# vk-sdk
Python SDK for vk.com API

### Wrapping  
just for making requests to the API and not using models, 
pass your parameters as strings or numbers to any method.

```python
import vkapi  
api = vkapi.API()  
api.Newsfeed.search(q='query')
```
  
or you can directly use subclasses

```python
import vkapi
newsfeed = vkapi.Newsfeed()  
newsfeed.search(q='query')
```