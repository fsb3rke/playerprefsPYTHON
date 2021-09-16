# playerprefsPYTHON

<li>main.py file is test file</li>
<li>playerprefsLib.py file is module file</li>

## NEWS
added setbool() function
added getbool() function

## Usage

```python
import playerprefsLib

#string

#save string
playerprefsLib.playerprefs(STRING_KEY).savestring(STRING_VARIABLE)
#get string
playerprefsLib.playerprefs(STRING_KEY).getstring() #returns key string value

#int

#save int 
playerprefsLib.playerprefs(STRING_KEY).saveint(INTEGER_VARIABLE)
#get int
playerprefsLib.playerprefs(STRING_KEY).getint() #returns key integer value
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
