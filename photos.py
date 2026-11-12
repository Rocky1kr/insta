from fastapi import UploadFile
from pathlib import Path
import uuid
import shutil
from PIL import Image, ImageOps

Path('media').mkdir(exist_ok=True)

def save_photo(photo: UploadFile):
  # ext = Path(photo.filename).suffix # => image.jpeg
  # name = f'{uuid.uuid4().hex}{ext}' # => 395328e1f63.jpeg

  # with open(f'media/{name}', 'wb') as f:
  #   shutil.copyfileobj(photo.file, f)

  image = Image.open(photo.file)
  # 핸드폰 사진 회전문제
  image = ImageOps.exif_transpose(image)
  # png 파일 변환
  image = image.convert('RGB')

  image = ImageOps.fit(image, (1080, 1080))

  name = f'{uuid.uuid4().hex}.jpg'
  image.save(f'media/{name}')

  return f'/media/{name}'

