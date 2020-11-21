import logging

from achaea.basic import eqbal
from achaea.state import s
from client import c, echo, send

logger = logging.getLogger("achaea")


jester_action_triggers = [
    (
        r"^You reach out and bop (.*) on the nose with your blackjack.$",
        # bop'd someone!
        lambda m: logger.fighting(f"BOP'D {m[0]}"),
    ),
]
c.add_triggers(jester_action_triggers)

"""
Handspring           Leap at your foes in neighboring rooms.
Props                Wish for the props that every good jester needs.
Balloons             Take to the skies with balloons.
Slipperiness         Slip out of that which would bind you.
Giraffes             Twist a balloon into a giraffe.
Backflip             Flip over obstructions.
Hocuspocus           Cast coloured illusions to dazzle those about you.
Runaway              Make a swift retreat.
Concussionbomb       Momentarily stun everyone in the room.
Butterflybomb        Blast people from the skies and trees.
Balloonhandoff       Launch your foes to the clouds with a balloon.
Backhandspring       Leap out of the room striking someone on the way out.
Balancing            Maintain superior balance.
Envenom              Coat a weapon in venoms.
Smokebomb            Choke all in the room with a plume of smoke.
Juggling             The ancient art of juggling.
Webbomb              Explode strands of webbing to bind everyone in the room.
Acrobatics           Masterful footwork to make yourself a difficult target.
Vent                 Sometimes you have to just let it all out.
Badjoke              Strip defences with your terrible jokes alone.
Mickey               Slip someone a mickey.
Traps                The ability to search for traps in your location.
Disarm               Attempt to disarm a trap.
Graffiti             Scrawl messages on walls.
Somersault           Quickly somersault past obstructions.
Arrowcatch           Pluck arrows from the air.
Bananas              Litter the floor with banana peels.
Firecracker          Construct festive firecrackers.
Itchpowder           Employ the irritating itchpowder.
Dustbomb             Numb the sense of your victims with a bomb.
Jackinthebox         An innocent musical toy with a vicious bite!
Timers               Give your bombs a delayed effect.
Gallowshumour        A tough crowd, this one.
Suicidemice          Brainwash mice to carry bombs on their backs.
Liberate             They weren't using it anyway.
"""
