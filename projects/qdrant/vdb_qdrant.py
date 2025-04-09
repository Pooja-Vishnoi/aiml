# Refer - https://qdrant.tech/documentation/quickstart/
# Installation
# docker pull qdrant/qdrant
# docker run -p 6333:6333 -p 6334:6334 \
#     -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
#     qdrant/qdrant
# python -m pip install qdrant_client

# Initialize the client
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct
from qdrant_client.models import Filter, FieldCondition, MatchValue

# client = QdrantClient(host="localhost", port=6333)
client = QdrantClient(url="http://localhost:6333")
# To enable collection uploading with grpc, use followinh initialization
# client = QdrantClient(host="localhost", grpc_port=6334, prefer_grpc=True)


def q_create_collection(collection_name, vectors_config):
    client.create_collection(
        collection_name=collection_name,
        vectors_config=vectors_config,
    )

# Add vector
def q_insert_vector(collection_name, points):
    operation_info = client.upsert(
        collection_name=collection_name,
        wait=True,
        points=points,
        )

    print(operation_info)

# run a query to search vector using query_points
def q_query_run(collection_name, query, limit, query_filter=None, with_payload=False):
    search_result = client.query_points(
        collection_name=collection_name,
        query=query,
        query_filter=query_filter,
        with_payload=with_payload,
        limit=limit,
    ).points

    print(search_result)

def q_insert_doc(collection_name, docs, metadata, ids):
    client.add(
        collection_name=collection_name,
        documents=docs,
        metadata=metadata,
        ids=ids
    )

# run a query to search vector using query
def q_query_doc(collection_name, query_text):
    search_result = client.query(
        collection_name=collection_name,
        query_text=query_text
    )
    print(search_result)

# Call Methods -------------------------------------------------------------------------
# EXAMPLE - 1
# q_create_collection("test_collection", VectorParams(size=4, distance=Distance.DOT))
# points=[
#                 PointStruct(id=1, vector=[0.05, 0.61, 0.76, 0.74], payload={"city": "Berlin"}),
#                 PointStruct(id=2, vector=[0.19, 0.81, 0.75, 0.11], payload={"city": "London"}),
#                 PointStruct(id=3, vector=[0.36, 0.55, 0.47, 0.94], payload={"city": "Moscow"}),
#                 PointStruct(id=4, vector=[0.18, 0.01, 0.85, 0.80], payload={"city": "New York"}),
#                 PointStruct(id=5, vector=[0.24, 0.18, 0.22, 0.44], payload={"city": "Beijing"}),
#                 PointStruct(id=6, vector=[0.35, 0.08, 0.11, 0.44], payload={"city": "Mumbai"}),
#             ]
# q_insert_vector("test_collection", points)
# query_filter=Filter(
#             must=[FieldCondition(key="city", match=MatchValue(value="London"))]
#         )
# q_query_run("test_collection", [0.2, 0.1, 0.9, 0.7], 3)
# q_query_run("test_collection", [0.2, 0.1, 0.9, 0.7], 3, query_filter=query_filter, with_payload=True)

# ----------------------------------------------------------------------------------------------
# EXAMPLE - 2
## pip install qdrant-client[fastembed]
# insert documents by first converting them to embeddings using fastembed
# docs = ["Qdrant has Langchain integrations", "Qdrant also has Llama Index integrations"]
# metadata = [{"source": "Langchain-docs"}, {"source": "Linkedin-docs"},]
# ids = [42, 2]
# q_insert_doc("demo_collection", docs, metadata, ids)
# q_query_doc("demo_collection", "This is a query document")


# --------------------
# EXAMPLE - 3
import numpy as np
from qdrant_client.models import Filter, FieldCondition, Range

# q_create_collection("my_collection", VectorParams(size=100, distance=Distance.COSINE))

# vectors = np.random.rand(100, 100)
# points=[
#         PointStruct(
#             id=idx,
#             vector=vector.tolist(),
#             payload={"color": "red", "rand_number": idx % 10}
#         )
#         for idx, vector in enumerate(vectors)
#     ]
# q_insert_vector("my_collection", points)

query_vector = np.random.rand(100)
q_query_run("my_collection", np.random.rand(100), 5)

query_filter=Filter(
        must=[  # These conditions are required for search results
            FieldCondition(
                key='rand_number',  # Condition based on values of `rand_number` field.
                range=Range(
                    gte=3  # Select only those results where `rand_number` >= 3
                )
            )
        ]
    )
q_query_run("my_collection", np.random.rand(100), 5, query_filter=query_filter, with_payload=True)

# try async - https://github.com/qdrant/qdrant-client    scroll to bottom for example





