[![Build](https://github.com/hushh-labs/hushh-vibe-catalog-reader/actions/workflows/main.yml/badge.svg)](https://github.com/hushh-labs/hushh-vibe-catalog-reader/actions/workflows/main.yml)
# hushh-vibe-catalog-reader
Support clients for the hushh vibe-catalog file format

# Schema
```flatbuffer
namespace hushh.hcf;

table Product {
  id: string;
  description: string;
  url: string;
  categories: [Category];
  vibes: [Vibe];
}

table Category {
  id: string;
  description: string;
  url: string;
  embeddings: [Embedding];
}

table Embedding {
    v:[float];
}

table Vibe {
  id: string;
  description: string;
  image_base64: string;
  url: string;
  embeddings: [Embedding];
}

table Catalog {
  id : string;
  version: string;
  description: string;
  products: [Product];
}

root_type Catalog;
```
