# b64!
[![Python 3.7.1](https://img.shields.io/badge/Python-3.7.1-green.svg)](http://www.python.org/download/)

convert offline/online data to base64 clean, fast and easy

what b64 do for you?
----
* clean, fast and easy
* convert data (image, video, text) to base64 from URL or local or b'string'
* convert base64 to data (image, video, text)
* auto-detect source type all you have to do is inserting the source
* support proxies, custom success code
* convert data to html(base64) tags, and data_uri
## install
You can either install from pypi or the source code
1) Using pip
```bash
pip install b64
```
2) from the source code
```bash
git clone https://github.com/n0x1s/b64
cd b64
python setup.py install
```
## How to use
### 1) Converting local/remote images/text ... to base64 and the opposite
Let us suppose you have a group of data that you want to convert to base64 or the opposite
```python
>>> from b64 import B64
### some examples ####
>>> online_image = 'https://avatars3.githubusercontent.com/u/1'
>>> local_image = 'test.jpg'
>>> string = 'hello'.encode()
>>> online_base64 = 'https://pastebin.com/raw/mYPrvzDz'
>>> local_base64 = 'example.txt'
>>> b64_string = b'aGVsbG8='
```
1) converting online data
```python
>>> B64(online_image).data # converting image to base64
> b'iVBORw0KGgoAAAANSUhEUgAAAcwAAAHMCAYAAABY25iGA...'
>>> B64('https://pastebin.com/raw/mYPrvzDz', to='string', codes=[200, 201]).data # you can set the success http codes or use proxies
> b'Hello'
```
2) converting local data
```python
>>> B64(local_image).data # converting image to base64
> b'iVBORw0KGgoAAAANSUhEUgAAAcwAAAHMCAYAAABY25iGA...'
>>> B64('example.txt', to='string').data # converting local base64 string to bytes
> b'Hello'
```
### 2) convert videos/images/css/js ... to html tag
```python
>>> from b64 import Tag64
>>> t = Tag64('https://avatars3.githubusercontent.com/u/1', 'img')
>>> t.html_tag
> '<img src="data:;base64,/9j/4AAQSkZJRgABAQAAAQA...'
>>> t.data_uri
> b'iVBORw0KGgoAAAANSUhEUgAAAcwAAAHMCAYAAABY25iGA...'

```
## Todo
I will try to maintain this respiratory and update or add new things to it you are welcome to contribute :relaxed:

And, as always have a beautiful day!
