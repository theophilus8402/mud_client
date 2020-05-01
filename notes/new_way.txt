
* have any server input (triggers/gmcp) return a dictionary
* have any user input (aliases) return a dictionary
* these dictionaries will look the same
* example:
{
    "var1" : value1,
    "var2" : value2,
    "add_temp_trigger" : temp_trig,
    "remove_temp_trigger" : temp_trigger(_name?),
    "add_echo" : echo_msg,
    "add_send_msg" : send_msg,
    "add_timer" : timer,
    "remove_timer" : timer,
}
* this way, I see ALL the outputs

