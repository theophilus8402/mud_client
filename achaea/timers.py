
import asyncio

from client import echo

#TODO: move to client/

class Timers():

    def __init__(self):
        self.timers = {}

    def add(self, name, action, wait_time, recurring=False):

        # see if there'a timer that already exists with that name
        if name in self.timers:
            # task.cancel() that task
            task = self.timers[name]
            task.cancel()

        # create a new async function that would  handle the timer
        if recurring:
            async_func = self.create_recurring_timer
        else:
            async_func = self.create_simple_timer

        # add the timer to the asyncio loop
        task = asyncio.ensure_future(async_func(name, action, wait_time))

        # add it to the timers dictionary
        self.timers[name] = task

    def remove(self, name):

        # if the named task is in there, cancel the task and remove it
        if name in self.timers:
            self.timers[name].cancel()

    async def create_simple_timer(self, name, action, wait_time):

        await asyncio.sleep(wait_time)
        action()

        # once the action is done, remove it from the timers dict
        echo(f"removing {name}!")
        del(self.timers[name])

    async def create_recurring_timer(self, name, action, wait_time):

        try:
            while True:
                await asyncio.sleep(wait_time)
                action()
        except:
            pass
        finally:
            echo(f"removing {name}!")
            # once the action is done, remove it from the timers dict
            del(self.timers[name])


timers = Timers()


if __name__ == "__main__":

    def kill(task):
        print("killing recurring task!")
        task.cancel()

    loop = asyncio.get_event_loop()
    timers.add("hello", lambda: print("hello!"), 3, recurring=True)
    hello_task = timers.timers["hello"]
    timers.add("kill_hello", lambda: kill(hello_task), 7, recurring=False)
    timers.add("kill_loop", lambda: loop.stop(), 10, recurring=False)
    loop.run_forever()

