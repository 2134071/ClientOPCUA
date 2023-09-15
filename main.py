import asyncio
import time
from asyncua import Client


async def main():
    client = Client("opc.tcp://10.4.1.128:4840")
    await client.connect()

    led1 = await client.nodes.objects.get_child("2:LED1")

    while True:
        time.sleep(0.5)
        command = input("Entrez une commande (R/G/B/F/Q pour quitter): ")

        if command == "R":
                    #.then == 2 await
            lumiereRouge = await (await led1.get_child("2:Rouge")).read_value()
            await (await led1.get_child("2:Rouge")).write_value(not lumiereRouge)
        elif command == "G":
            lumiereGreen = await (await led1.get_child("2:Green")).read_value()
            await (await led1.get_child("2:Green")).write_value(not lumiereGreen)
        elif command == "B":
            lumiereBlue = await (await led1.get_child("2:Blue")).read_value()
            await (await led1.get_child("2:Blue")).write_value(not lumiereBlue)
        elif command == "F":
            await led1.call_method("2:toggleFermerLumiere")
        elif command == "Q":
            break
        else:
            print("Commande non reconnue.")

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())