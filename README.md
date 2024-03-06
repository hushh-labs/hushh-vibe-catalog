[![Build](https://github.com/hushh-labs/hushh-vibe-catalog-reader/actions/workflows/main.yml/badge.svg)](https://github.com/hushh-labs/hushh-vibe-catalog-reader/actions/workflows/main.yml)
# hushh-vibe-catalog
Support clients for the hushh vibe-catalog file format

There is documentation [available](https://hushh-labs.github.io/hushh-vibe-catalog-reader/reference)


# Installation
```python3
$> pip install hushh-vibe-catalog

```

# Latest Version Schema
```flatbuffer

namespace hushh.hcf;

table Product {
  id: string;
  description: string;
  url: string;
}

table Vibe {
  id: string;
  description: string;
  product_idx: [int];
}

table Category {
  id: string;
  description: string;
  url: string;
  product_idx: [int];
}

enum VibeMode : byte { ProductText = 0, ProductImage, Text, Image, Category}

table FlatEmbeddingBatch {
    id: string;
    shape:[int];
    type: VibeMode;
    flat_tensor:[float];
}

table ProductVibes {
  id: string;
  products: [Product];
  categories: [Category];
  vibes: [Vibe];
  flat_batches: [FlatEmbeddingBatch];
}

table Catalog {
  id : string;
  version: string;
  description: string;
  product_vibes: ProductVibes;
}

root_type Catalog;
```


# Better documentation coming soon!
I promise :)
