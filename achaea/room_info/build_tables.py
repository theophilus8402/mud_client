
from db import engine, Base, Session
from models import RoomInfo

Base.metadata.create_all(engine)

room = RoomInfo(num=26757,
                name="Grand Dome of the Aegean Manor (indoors)",
                desc="Formed into a perfect dome overhead, polished panes of obsidian are locked into place with thin strips of sparkling mithril. The surrounding torchlight glints off the reflective stone creating a bright aura about the chamber, every nook and cranny cleaned meticulously so that no dust begins to gather. A pair of immense golden doors lead out of the chamber to east, elaborate engravings covering every inch of the opulent metal. Lavish linens spread across wide chairs situated along the outside walls, reserved for emissaries waiting to meet with the Lord of Warfare in His chambers. Servants dash quickly across the vast dome and into other areas of the keep, a few lone acolytes shouting orders to the passing peasants and pointing them to their next assignments.",
                area="the Temple of War",
                environment="Urban",
                coords="341,2,0,0",
                map="www.achaea.com/irex/maps/clientmap.php?map=341&building=0&level=0 7 2",
                details='[ "indoors" ]',
                exits='{ "ne": 26369, "se": 26837, "sw": 26380, "w": 24970, "nw": 26944 }'
                )

session = Session()

session.add(room)
session.commit()

