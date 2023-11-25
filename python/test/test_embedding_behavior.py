# import requests
# from PIL import Image
# from transformers import CLIPModel, CLIPProcessor

# model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
# processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# from hushh.catalog import Catalog, Category, Embedding, Product, Vibe
# from hushh.hcf import Catalog as RawCatalog


# def get_embeddings():
#     with open("embed_images/cat-with-open-mouth.webp", "rb") as fh:
#         cat = Image.open(fh)

#     with open("embed_images/portrait-of-a-pug-dog-wearing-bow-tie.webp", "rb") as fh:
#         dog = Image.open(fh)

#     with open("embed_images/soccer-ball.webp", "rb") as fh:
#         soccer = Image.open(fh)

#     with open("embed_images/strawberry.webp", "rb") as fh:
#         berry = Image.open(fh)

#     inputs = processor(
#         text=[
#             "a photo of a cat",
#             "a photo of a dog",
#             "a photo of a soccer ball",
#             "a photo of a strawberry",
#         ],
#         images=[cat, dog, soccer, berry],
#         return_tensors="pt",
#         padding=True,
#     )

#     outputs = model(**inputs)

#     logits_per_image = (
#         outputs.logits_per_image
#     )  # this is the image-text similarity score
#     probs = logits_per_image.softmax(
#         dim=1
#     )  # we can take the softmax to get the label probabilities
#     assert probs[0][0] > probs[0][1]
#     assert outputs.image_embeds.shape[0] == 4
#     return outputs.image_embeds


# def test_embeds():
#     pass
#     # embeds = get_embeddings()
#     # import pdb

#     # pdb.set_trace()
#     # assert True
