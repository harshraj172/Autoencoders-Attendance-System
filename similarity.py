# -*- coding: utf-8 -*-
"""similarity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fbwrjoZnc6D2LNe8z75bGdrPPf9gF3ak
"""

def similarity_score(ref_image, selfie_images, device):
    """
    Given an image and number of similar images to search.
    Returns the num_images closest neares images.
    Args:
    image: Image whose similar images are to be found.
    num_images: Number of similar images to find.
    embedding : A (num_images, embedding_dim) Embedding of images learnt from auto-encoder.
    device : "cuda" or "cpu" device.
    """
    # for ref_image
    ref_image_tensor = T.ToTensor()(ref_image)
    ref_image_tensor = ref_image_tensor.unsqueeze(0)
    
    # for selfie_image
    selfie_image_tensor = T.ToTensor()(selfie_image)
    selfie_image_tensor = selfie_image_tensor.unsqueeze(0)

    with torch.no_grad():
        ref_image_embedding = encoder(ref_image_tensor).cpu().detach().numpy()
        selfie_image_embedding = encoder(selfie_image_tensor).cpu().detach().numpy()
        
    ref_flattened_embedding = image_embedding.reshape((ref_image_embedding.shape[0], -1))
    selfie_flattened_embedding = image_embedding.reshape((selfie_image_embedding.shape[0], -1))

    cosine_score = distance.cosine(ref_flattened_embedding, selfie_flattened_embedding)
    return cosine_score