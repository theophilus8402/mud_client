
import asyncio
import logging
import time

from .client import c, echo
from .state import s

logger = logging.getLogger("achaea")

"""
You remove 1 echinacea, bringing the total in the rift to 173.
You eat an echinacea root.
You now possess the gift of the third eye.
4000h, 4801m, 15200e, 19640w exdb-

You have recovered balance on all limbs.
4000h, 4801m, 15200e, 19640w exdb-

You eat a hawthorn berry.
4000h, 4801m, 15200e, 19640w exb-
You remove 1 hawthorn berry, bringing the total in the rift to 174.
4000h, 4801m, 15200e, 19640w exb-
You eat a hawthorn berry.
The plant has no effect.
4000h, 4801m, 15200e, 19640w exb-
You may eat another plant or mineral.
4000h, 4801m, 15200e, 19640w exb-
Woo!  We've gained deafness!
You have been afflicted with deafness.
The aural world fades to silence.


You take a drink from a pinewood vial.
The elixir heals and soothes you.
4000h, 4651m, 15200e, 19640w exdb-
You may drink another health or mana elixir.


You have no pipes that require lighting.
You take a long drag of skullcap off your pipe.
4000h, 4651m, 15200e, 19640w exdb-
Your lungs have recovered enough to smoke another mineral or plant.
4000h, 4651m, 15200e, 19640w exdb-


Lost HERB: a black cohosh root?
You remove 1 black cohosh, bringing the total in the rift to 188.
You eat a black cohosh root.
You have been afflicted with insomnia.
You suddenly feel incapable of falling asleep.
4000h, 4651m, 15200e, 19640w exdb-
Woo!  We've gained kola!
Lost HERB: a kola nut?
You remove 1 kola nut, bringing the total in the rift to 136.
You eat a kola nut.
An instant feeling of excitement and edginess overcomes you.
4000h, 4651m, 15200e, 19640w exkdb-
Woo!  We've gained deathsight!
Lost HERB: a skullcap flower?


Herbs which do not remove herb balance:
    echinacea
    kola
    cohosh
    skullcap


You take out some salve and quickly rub it on your skin.
You messily spread the salve over your body, to no effect.

You take out some salve and quickly rub it on your skin.
The salve dissolves and quickly disappears after you apply it.

You may apply another salve to yourself.


"""


def set_display_balance_timer(matches):
    if matches == "on":
        echo("Turning on balance timer!")
        s.show_balance_times = True
    elif matches == "off":
        echo("Turning on balance timer!")
        s.show_balance_times = False

balance_aliases = [
    (   "^btimer (.*)$",
        "btimer on/off - balance timer",
        lambda matches: set_display_balance_timer(matches[0])
    ),
]
c.add_aliases("balance", balance_aliases)


def create_end_timer(timer_type, end_msg):
    start_time = time.time()

    def tmp_trig(matches):
        total = time.time() - start_time
        echo(f"{timer_type}: {total:0.2}s")
        c.remove_temp_trigger(timer_type)
    timer_trig = (end_msg, tmp_trig)
    c.add_temp_trigger(timer_type, timer_trig)


def recovered_eq(matches):
    #echo("Got EQ back!")
    logger.fighting("You have recovered equilibrium")


def recovered_bal(matches):
    #echo("Got BAL back!")
    logger.fighting("You have recovered balance on all limbs.")


def recovered_herb(matches):
    #echo("Got HERB back!")
    pass


def lost_elixir(matches):
    #echo("Lost sip balance!!")
    if s.show_balance_times:
        end_msg = r"^You may drink another health or mana elixir.$"
        create_end_timer("herb", end_msg)


def recovered_elixir(matches):
    #echo("Got ELIXIR back!")
    pass


def lost_smoke(matches):
    if s.show_balance_times:
        end_msg = r"^Your lungs have recovered enough to smoke another mineral or plant.$"
        create_end_timer("smoke", end_msg)


def recovered_smoke(matches):
    #echo("Got SMOKE back!")
    pass


def lost_herb(herb):
    herbs_no_loss = [   "an echinacea root",
                        "a black cohosh root",
                        "a kola nut",
                        "a skullcap flower",
                        ]
    if herb in herbs_no_loss:
        #echo("Didn't lose herb balance!")
        return False

    # see if we ate an herb off balance
    if "The plant has no effect." in c.current_chunk:
        #echo("Ate an herb off balance!!")
        return False

    #echo(f"Lost HERB: {herb}!")

    if s.show_balance_times:
        end_msg = r"^You may eat another plant or mineral.$"
        create_end_timer("herb", end_msg)


def recovered_salve(matches):
    #echo("Got SALVE back!")
    pass


def lost_salve(matches):
    if "The salve dissolves and quickly disappears after you apply it." in c.current_chunk:
        #echo("Applied salve off balance!")
        return False

    #echo("Lost SALVE!")
    if s.show_balance_times:
        end_msg = r"^You may apply another salve to yourself.$"
        create_end_timer("salve", end_msg)


balance_triggers = [
    (   r"^You are not fallen or kneeling.$",
        # I'm up!
        lambda m: c.delete_line()
    ),
    (   r"^You have recovered equilibrium.$",
        # eq back
        recovered_eq
    ),
    (   r"^You have recovered balance on all limbs.$",
        # bal back
        recovered_bal
    ),
    (   r"^You may eat another plant or mineral.$",
        # herb back
        recovered_herb
    ),
    (   r"^The elixir heals and soothes you.$",
        # elixir lost
        lost_elixir
    ),
    (   r"^Your mind feels stronger and more alert.$",
        # elixir lost
        lost_elixir
    ),
    (   r"^You may drink another health or mana elixir.$",
        # elixir back
        recovered_elixir
    ),
    (   r"^You take a long drag of (.*) off your pipe.$",
        # smoke lost
        lost_smoke
    ),
    (   r"^Your lungs have recovered enough to smoke another mineral or plant.$",
        # smoke back
        recovered_smoke
    ),
    (   r"^You eat (.*).$",
        # herb lost
        lambda matches: lost_herb(matches[0])
    ),
    (   r"^You take out some salve and quickly rub it on your skin.$",
        # salve lost
        lost_salve
    ),
    (   r"^You may apply another salve to yourself.$",
        # salve back
        recovered_salve
    ),
]
c.add_triggers(balance_triggers)


def gmcp_bal_eq(gmcp_data):
    bal = gmcp_data.get("bal")
    eq = gmcp_data.get("eq")

    if bal == "1" and s.bal == "0":
        #echo("Got back balance!")
        pass
    elif bal == "0" and s.bal == "1":
        #echo("Lost balance!")

        # time how long it takes
        if s.show_balance_times:
            end_msg = r"^You have recovered balance on all limbs.$"
            create_end_timer("bal", end_msg)

    if eq == "1" and s.eq == "0":
        #echo("Got back eq!")
        pass
    elif eq == "0" and s.eq == "1":
        #echo("Lost eq!")

        # time how long it takes
        if s.show_balance_times:
            end_msg = r"^You have recovered equilibrium.$"
            create_end_timer("eq", end_msg)

    s.bal = bal
    s.eq = eq
c.add_gmcp_handler("Char.Vitals", gmcp_bal_eq)
