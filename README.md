# GraphQL Flask Example

This repository contains a simple example of how to use GraphQL with Flask. GraphQL is a query language for your API and a server-side runtime for executing queries by using a type system you define for your data. GraphQL isn't tied to any specific database or storage engine and is instead backed by your existing code and data.

## Quick Explanation of GraphQL

GraphQL is a powerful tool that allows clients to request exactly the data they need, and nothing more. It enables declarative data fetching, where a client can specify not only the data they want but also the format of the response. This can lead to more efficient data retrieval and reduce the amount of data transferred over the network.

Key benefits of GraphQL:
- **Declarative Data Fetching:** Clients can specify exactly what data they need.
- **Single Endpoint:** Unlike REST, which often requires multiple endpoints, GraphQL typically uses a single endpoint.
- **Strongly Typed:** GraphQL schemas are strongly typed, which makes it easier to validate and understand the data.

## Required Pip Installs

To set up the environment for this project, you need to install several Python packages. Here is a list of the required pip installs:

```sh
pip install flask
pip install flask-sqlalchemy
pip install flask-migrate
pip install graphene
pip install --pre graphene-sqlalchemy
pip install "graphql-server[flask]"
```