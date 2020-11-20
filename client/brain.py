
import traceback

class Brain():

    def __init__(self, client):
        self.client = client

    def handle_aliases(self, msg):

        alias_handled = False
        #for compiled_pattern, action in self.aliases:
        for compiled_pattern, action in self.client._aliases:
            match = compiled_pattern.match(msg)
            if match:
                action(match.groups())
                alias_handled = True
                break

        return alias_handled

    def handle_triggers(self, msg):

        trig_handled = False

        #for compiled_pattern, action in self.triggers:
        for search_method, action in self.client._triggers:
            #match = compiled_pattern.match(msg)
            match = search_method(msg)
            if match:
                #c.echo(match.re.pattern)
                try:
                    action(match.groups())
                    trig_handled = True
                except Exception as e:
                    print(f"handle_triggers: {e}")

        return trig_handled

    def handle_gmcp(self, gmcp_type, gmcp_data):
        try:
            for gmcp_handler in self.client._gmcp_handlers.get(gmcp_type, []):
                gmcp_handler(gmcp_data)
            #basic.echo(f"{gmcp_type} : {gmcp_data}")
        except Exception as e:
            print(f"problem with __init__.handle_gmcp {e}")
            traceback.print_exc(file=sys.stdout)

