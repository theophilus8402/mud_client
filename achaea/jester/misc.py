from client import c, send

misc_aliases = [
    (
        "^he$",
        "say house phrase",
        lambda matches: send("speak mhaldorian;say Evil subjugates all things."),
    ),
]
c.add_aliases("sarmenti_misc", misc_aliases)
