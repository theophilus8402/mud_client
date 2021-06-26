from achaea.basic import eqbal
from achaea.state import s
from client import c, send

weaponmastery_aliases = [
   (
       "^m$",
       "stand;combination &tar slice smash",
       lambda m: eqbal("stand;combination &tar slice smash"),
   ),
   (
       "^ra$",
       "stand;combination &tar raze smash mid",
       lambda m: eqbal("stand;combination &tar raze smash mid"),
   ),
   (
       "^cah$",
       "stand;combination &tar slice aconite smash high",
       lambda m: eqbal("stand;combination &tar slice aconite smash high"),
   ),
   (
       "^cam$",
       "stand;combination &tar slice aconite smash mid",
       lambda m: eqbal("stand;combination &tar slice aconite smash mid"),
   ),
   (
       "^cal$",
       "stand;combination &tar slice aconite smash low",
       lambda m: eqbal("stand;combination &tar slice aconite smash low"),
   ),
   (
       "^cad$",
       "stand;combination &tar slice aconite drive",
       lambda m: eqbal("stand;combination &tar slice aconite drive"),
   ),
   (
       "^cac$",
       "stand;combination &tar slice aconite concuss",
       lambda m: eqbal("stand;combination &tar slice aconite concuss"),
   ),
   (
       "^cat$",
       "stand;combination &tar slice aconite trip",
       lambda m: eqbal("stand;combination &tar slice aconite trip"),
   ),
   (
       "^cab$",
       "stand;combination &tar slice aconite club",
       lambda m: eqbal("stand;combination &tar slice aconite club"),
   ),
   (
       "^cch$",
       "stand;combination &tar slice curare smash high",
       lambda m: eqbal("stand;combination &tar slice curare smash high"),
   ),
   (
       "^ccm$",
       "stand;combination &tar slice curare smash mid",
       lambda m: eqbal("stand;combination &tar slice curare smash mid"),
   ),
   (
       "^ccl$",
       "stand;combination &tar slice curare smash low",
       lambda m: eqbal("stand;combination &tar slice curare smash low"),
   ),
   (
       "^ccd$",
       "stand;combination &tar slice curare drive",
       lambda m: eqbal("stand;combination &tar slice curare drive"),
   ),
   (
       "^ccc$",
       "stand;combination &tar slice curare concuss",
       lambda m: eqbal("stand;combination &tar slice curare concuss"),
   ),
   (
       "^cct$",
       "stand;combination &tar slice curare trip",
       lambda m: eqbal("stand;combination &tar slice curare trip"),
   ),
   (
       "^ccb$",
       "stand;combination &tar slice curare club",
       lambda m: eqbal("stand;combination &tar slice curare club"),
   ),
   (
       "^csh$",
       "stand;combination &tar slice slike smash high",
       lambda m: eqbal("stand;combination &tar slice slike smash high"),
   ),
   (
       "^csm$",
       "stand;combination &tar slice slike smash mid",
       lambda m: eqbal("stand;combination &tar slice slike smash mid"),
   ),
   (
       "^csl$",
       "stand;combination &tar slice slike smash low",
       lambda m: eqbal("stand;combination &tar slice slike smash low"),
   ),
   (
       "^csd$",
       "stand;combination &tar slice slike drive",
       lambda m: eqbal("stand;combination &tar slice slike drive"),
   ),
   (
       "^csc$",
       "stand;combination &tar slice slike concuss",
       lambda m: eqbal("stand;combination &tar slice slike concuss"),
   ),
   (
       "^cst$",
       "stand;combination &tar slice slike trip",
       lambda m: eqbal("stand;combination &tar slice slike trip"),
   ),
   (
       "^csb$",
       "stand;combination &tar slice slike club",
       lambda m: eqbal("stand;combination &tar slice slike club"),
   ),
   (
       "^ckh$",
       "stand;combination &tar slice kalmia smash high",
       lambda m: eqbal("stand;combination &tar slice kalmia smash high"),
   ),
   (
       "^ckm$",
       "stand;combination &tar slice kalmia smash mid",
       lambda m: eqbal("stand;combination &tar slice kalmia smash mid"),
   ),
   (
       "^ckl$",
       "stand;combination &tar slice kalmia smash low",
       lambda m: eqbal("stand;combination &tar slice kalmia smash low"),
   ),
   (
       "^ckd$",
       "stand;combination &tar slice kalmia drive",
       lambda m: eqbal("stand;combination &tar slice kalmia drive"),
   ),
   (
       "^ckc$",
       "stand;combination &tar slice kalmia concuss",
       lambda m: eqbal("stand;combination &tar slice kalmia concuss"),
   ),
   (
       "^ckt$",
       "stand;combination &tar slice kalmia trip",
       lambda m: eqbal("stand;combination &tar slice kalmia trip"),
   ),
   (
       "^ckb$",
       "stand;combination &tar slice kalmia club",
       lambda m: eqbal("stand;combination &tar slice kalmia club"),
   ),
   (
       "^cgh$",
       "stand;combination &tar slice gecko smash high",
       lambda m: eqbal("stand;combination &tar slice gecko smash high"),
   ),
   (
       "^cgm$",
       "stand;combination &tar slice gecko smash mid",
       lambda m: eqbal("stand;combination &tar slice gecko smash mid"),
   ),
   (
       "^cgl$",
       "stand;combination &tar slice gecko smash low",
       lambda m: eqbal("stand;combination &tar slice gecko smash low"),
   ),
   (
       "^cgd$",
       "stand;combination &tar slice gecko drive",
       lambda m: eqbal("stand;combination &tar slice gecko drive"),
   ),
   (
       "^cgc$",
       "stand;combination &tar slice gecko concuss",
       lambda m: eqbal("stand;combination &tar slice gecko concuss"),
   ),
   (
       "^cgt$",
       "stand;combination &tar slice gecko trip",
       lambda m: eqbal("stand;combination &tar slice gecko trip"),
   ),
   (
       "^cgb$",
       "stand;combination &tar slice gecko club",
       lambda m: eqbal("stand;combination &tar slice gecko club"),
   ),
   (
       "^cxh$",
       "stand;combination &tar slice xentio smash high",
       lambda m: eqbal("stand;combination &tar slice xentio smash high"),
   ),
   (
       "^cxm$",
       "stand;combination &tar slice xentio smash mid",
       lambda m: eqbal("stand;combination &tar slice xentio smash mid"),
   ),
   (
       "^cxl$",
       "stand;combination &tar slice xentio smash low",
       lambda m: eqbal("stand;combination &tar slice xentio smash low"),
   ),
   (
       "^cxd$",
       "stand;combination &tar slice xentio drive",
       lambda m: eqbal("stand;combination &tar slice xentio drive"),
   ),
   (
       "^cxc$",
       "stand;combination &tar slice xentio concuss",
       lambda m: eqbal("stand;combination &tar slice xentio concuss"),
   ),
   (
       "^cxt$",
       "stand;combination &tar slice xentio trip",
       lambda m: eqbal("stand;combination &tar slice xentio trip"),
   ),
   (
       "^cxb$",
       "stand;combination &tar slice xentio club",
       lambda m: eqbal("stand;combination &tar slice xentio club"),
   ),
   (
       "^cph$",
       "stand;combination &tar slice prefarar smash high",
       lambda m: eqbal("stand;combination &tar slice prefarar smash high"),
   ),
   (
       "^cpm$",
       "stand;combination &tar slice prefarar smash mid",
       lambda m: eqbal("stand;combination &tar slice prefarar smash mid"),
   ),
   (
       "^cpl$",
       "stand;combination &tar slice prefarar smash low",
       lambda m: eqbal("stand;combination &tar slice prefarar smash low"),
   ),
   (
       "^cpd$",
       "stand;combination &tar slice prefarar drive",
       lambda m: eqbal("stand;combination &tar slice prefarar drive"),
   ),
   (
       "^cpc$",
       "stand;combination &tar slice prefarar concuss",
       lambda m: eqbal("stand;combination &tar slice prefarar concuss"),
   ),
   (
       "^cpt$",
       "stand;combination &tar slice prefarar trip",
       lambda m: eqbal("stand;combination &tar slice prefarar trip"),
   ),
   (
       "^cpb$",
       "stand;combination &tar slice prefarar club",
       lambda m: eqbal("stand;combination &tar slice prefarar club"),
   ),
   (
       "^cdh$",
       "stand;combination &tar slice digitalis smash high",
       lambda m: eqbal("stand;combination &tar slice digitalis smash high"),
   ),
   (
       "^cdm$",
       "stand;combination &tar slice digitalis smash mid",
       lambda m: eqbal("stand;combination &tar slice digitalis smash mid"),
   ),
   (
       "^cdl$",
       "stand;combination &tar slice digitalis smash low",
       lambda m: eqbal("stand;combination &tar slice digitalis smash low"),
   ),
   (
       "^cdd$",
       "stand;combination &tar slice digitalis drive",
       lambda m: eqbal("stand;combination &tar slice digitalis drive"),
   ),
   (
       "^cdc$",
       "stand;combination &tar slice digitalis concuss",
       lambda m: eqbal("stand;combination &tar slice digitalis concuss"),
   ),
   (
       "^cdt$",
       "stand;combination &tar slice digitalis trip",
       lambda m: eqbal("stand;combination &tar slice digitalis trip"),
   ),
   (
       "^cdb$",
       "stand;combination &tar slice digitalis club",
       lambda m: eqbal("stand;combination &tar slice digitalis club"),
   ),
   (
       "^cesh$",
       "stand;combination &tar slice epseth smash high",
       lambda m: eqbal("stand;combination &tar slice epseth smash high"),
   ),
   (
       "^cesm$",
       "stand;combination &tar slice epseth smash mid",
       lambda m: eqbal("stand;combination &tar slice epseth smash mid"),
   ),
   (
       "^cesl$",
       "stand;combination &tar slice epseth smash low",
       lambda m: eqbal("stand;combination &tar slice epseth smash low"),
   ),
   (
       "^cesd$",
       "stand;combination &tar slice epseth drive",
       lambda m: eqbal("stand;combination &tar slice epseth drive"),
   ),
   (
       "^cesc$",
       "stand;combination &tar slice epseth concuss",
       lambda m: eqbal("stand;combination &tar slice epseth concuss"),
   ),
   (
       "^cest$",
       "stand;combination &tar slice epseth trip",
       lambda m: eqbal("stand;combination &tar slice epseth trip"),
   ),
   (
       "^cesb$",
       "stand;combination &tar slice epseth club",
       lambda m: eqbal("stand;combination &tar slice epseth club"),
   ),
   (
       "^ceth$",
       "stand;combination &tar slice epteth smash high",
       lambda m: eqbal("stand;combination &tar slice epteth smash high"),
   ),
   (
       "^cetm$",
       "stand;combination &tar slice epteth smash mid",
       lambda m: eqbal("stand;combination &tar slice epteth smash mid"),
   ),
   (
       "^cetl$",
       "stand;combination &tar slice epteth smash low",
       lambda m: eqbal("stand;combination &tar slice epteth smash low"),
   ),
   (
       "^cetd$",
       "stand;combination &tar slice epteth drive",
       lambda m: eqbal("stand;combination &tar slice epteth drive"),
   ),
   (
       "^cetc$",
       "stand;combination &tar slice epteth concuss",
       lambda m: eqbal("stand;combination &tar slice epteth concuss"),
   ),
   (
       "^cett$",
       "stand;combination &tar slice epteth trip",
       lambda m: eqbal("stand;combination &tar slice epteth trip"),
   ),
   (
       "^cetb$",
       "stand;combination &tar slice epteth club",
       lambda m: eqbal("stand;combination &tar slice epteth club"),
   ),
   (
       "^cvh$",
       "stand;combination &tar slice vernalius smash high",
       lambda m: eqbal("stand;combination &tar slice vernalius smash high"),
   ),
   (
       "^cvm$",
       "stand;combination &tar slice vernalius smash mid",
       lambda m: eqbal("stand;combination &tar slice vernalius smash mid"),
   ),
   (
       "^cvl$",
       "stand;combination &tar slice vernalius smash low",
       lambda m: eqbal("stand;combination &tar slice vernalius smash low"),
   ),
   (
       "^cvd$",
       "stand;combination &tar slice vernalius drive",
       lambda m: eqbal("stand;combination &tar slice vernalius drive"),
   ),
   (
       "^cvc$",
       "stand;combination &tar slice vernalius concuss",
       lambda m: eqbal("stand;combination &tar slice vernalius concuss"),
   ),
   (
       "^cvt$",
       "stand;combination &tar slice vernalius trip",
       lambda m: eqbal("stand;combination &tar slice vernalius trip"),
   ),
   (
       "^cvb$",
       "stand;combination &tar slice vernalius club",
       lambda m: eqbal("stand;combination &tar slice vernalius club"),
   ),
]
c.add_aliases("ab_weaponmastery", weaponmastery_aliases)
