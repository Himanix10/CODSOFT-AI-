!pip install transformers==4.40.0

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from IPython.display import display
from google.colab import files

# Load BLIP
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Upload an image
uploaded = files.upload()
img_path = next(iter(uploaded))

# Open & show image
raw_image = Image.open(img_path).convert('RGB')
display(raw_image)

# Caption
inputs = processor(raw_image, return_tensors="pt")
out = model.generate(**inputs)
print("Generated Caption:", processor.decode(out[0], skip_special_tokens=True))
