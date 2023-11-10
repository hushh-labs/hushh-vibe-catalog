[![Build](https://github.com/hushh-labs/hushh-vibe-catalog-reader/actions/workflows/main.yml/badge.svg)](https://github.com/hushh-labs/hushh-vibe-catalog-reader/actions/workflows/main.yml)
# hushh-vibe-catalog-reader
Support clients for the hushh vibe-catalog file format

# Schema
```flatbuffer
namespace hushh;

table ProductCharacterization {
  id: string;
  description: string;
  url: string;
  product_ids: [string];
}

table Product {
  id: string;
  description: string;
  url: string;
  characterization_ids: [string];
}

table Embedding {
    v:[float];
}

table ProductInformation {
  id: string;
  description: string;
  image_base64: string;
  url: string;
}

table CharacterizationEmbeddings {
  id: string;
  description: string;
  url: string;
}


table Catalog {
  id : string;
  version: string;
  head: string;
  products: [Product];
  product_embeddings: [Embedding];
  characterizations: [ProductCharacterization];
  characterization_embeddings: [Embedding];
  product_information: [ProductInformation];
}

root_type Catalog;
```
