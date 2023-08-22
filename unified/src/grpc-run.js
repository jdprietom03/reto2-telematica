import { Services } from "./grpc-services.js";
import { Run as RunAMQP } from "./amqp-run.js";
import util from "util";

export const Run = async (request, response) => {
    console.info("Consumer service is started...")

    const idProduct = 1;
    const client = Services.ProductService();

    try {
        const addProductPromise = util.promisify(client.AddProduct).bind(client);
        const result = await addProductPromise({ id_product: idProduct });

        response.json({ 
            message: "Response received from remote service:",
            data: result
        });
    } catch (error) {
        await handleFallback(request, response);
    }
}

const handleFallback = async (request, response) => {
    RunAMQP(request, response);
}