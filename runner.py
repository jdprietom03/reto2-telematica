import requests
import asyncio

class TokenBucket:
    def __init__(self, capacity, fill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.fill_rate = fill_rate
        self.last_update = asyncio.get_event_loop().time()

    def _refill(self, current_time):
        if current_time > self.last_update:
            elapsed_time = current_time - self.last_update
            new_tokens = elapsed_time * self.fill_rate
            self.tokens = min(self.capacity, self.tokens + new_tokens)
            self.last_update = current_time

    async def acquire(self):
        current_time = asyncio.get_event_loop().time()
        self._refill(current_time)

        while self.tokens < 1:
            await asyncio.sleep(0.01)
            current_time = asyncio.get_event_loop().time()
            self._refill(current_time)

        self.tokens -= 1

def hacer_solicitud(indice):
    url = f'http://localhost:80/grpc?id={indice}'
    response = requests.get(url)

    print(f'Solicitud {indice + 1}: Código de estado {response.status_code}, Respuesta: {response.text}', end = "\r")

    return response.status_code, response.text

async def realizar_solicitudes():
    num_solicitudes = 100
    rps = 10
    intervalo = 1 / rps

    token_bucket = TokenBucket(5, 300)

    resultados = []
    for indice in range(num_solicitudes):
        await token_bucket.acquire()
        tarea = asyncio.to_thread(hacer_solicitud, indice)
        resultados.append(tarea)

    return await asyncio.gather(*resultados)

async def main():
    resultados = await realizar_solicitudes()

asyncio.run(main())
