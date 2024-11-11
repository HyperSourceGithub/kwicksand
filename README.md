# kwiksand
### an efficient, simple text engine
types text character by character

# Kwikstart
```py
import kwiksand as k
k.kwik("Hello World!", 0.06, True)
```
Will type "Hello World!" with a 0.06 delay between characters, and regularly print the text if it's too long.
# Usage
```py
kwik(text, delay=0.04, overprint=False)
```
#### Parameters
`text`: the text you want to write.

`delay`: the delay between characters (sec). Default value is `0.04` seconds.

`overprint`: regularly prints text (`print()`) if it's too long when True. Default value is `False`.

# Examples
#### Basic
```py
kwik("hello")
# will type "hello" with a default of 0.05s delay between characters.
```
#### Predefined Text
```py
kwik("hello", 0.5)
# will type "hello" with a 0.5s delay between characters
```
