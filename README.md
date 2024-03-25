# Hushh Catalog Format


[![Build](https://github.com/hushh-labs/hushh-vibe-catalog-reader/actions/workflows/main.yml/badge.svg)](https://github.com/hushh-labs/hushh-vibe-catalog-reader/actions/workflows/main.yml)

Support clients for the hushh vibe-catalog file format

There is documentation
[available](https://hushh-labs.github.io/hushh-vibe-catalog-reader/)

# Installation

``` python3
$> pip install hushh-vibe-catalog
```

# Latest Version Schema

``` flatbuffer
namespace hushh.hcf;

table Brand {
  id: string;
  description: string;
  name: string;
  url: string;
}

table Product {
  id: string;
  description: string;
  url: string;
  brand: Brand;
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
    vibe_mode: VibeMode;
    flat_tensor:[float];
    product_idx: [int];
}

table ProductVibes {
  id: string;
  products: [Product];
  brands: [Brand];
  categories: [Category];
  vibes: [Vibe];
  product_text_batches: [FlatEmbeddingBatch];
  product_image_batches: [FlatEmbeddingBatch];
  text_batches: [FlatEmbeddingBatch];
  image_batches: [FlatEmbeddingBatch];
}

table Catalog {
  id : string;
  version: string;
  description: string;
  product_vibes: ProductVibes;
  batch_size: int;
  tokenizer_name_or_path: string;
  model_name_or_path: string;
}

root_type Catalog;
```
