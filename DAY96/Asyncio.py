import asyncio

# Async function -> runs with event loop
async def function1():
    await asyncio.sleep(1)   # non-blocking wait (1 sec)
    print("func 1")

async def function2():
    await asyncio.sleep(1)
    print("func 2")

async def function3():
    await asyncio.sleep(4)
    print("func 3")


async def main():

    # OLD WAY (commented):
    # create_task -> runs in background
    # but below awaits make execution mostly sequential

    # task = asyncio.create_task(function1())
    # await function2()   # waits for func2 to finish
    # await function3()   # then waits for func3
    # await task          # finally waits for func1


    # NEW WAY -> BEST WAY for parallel execution
    L = await asyncio.gather(
        function1(),
        function2(),   # all start together (parallel execution)
        function3(),
    )

    # L will store results (if functions return something)
    # here it will be [None, None, None] since no return


# Start the async program
asyncio.run(main())