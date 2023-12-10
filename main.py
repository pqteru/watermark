from PIL import Image, ImageDraw, ImageFont
import sys
import os

def compress_and_watermark_image(image_path):
    try: 
        # Open image and get dimensions
        with Image.open(image_path).convert("RGBA") as image:
            width, height = image.size

            # Determine ratio based on larger dimension
            ratio = max(width, height) / 1024

            # Resize image to fit ratio
            image = image.resize((int(width / ratio), int(height / ratio)))

            # Add watermark to image
            watermark = Image.new('RGBA', image.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(watermark)
            font = ImageFont.truetype("Impact.ttf", 18)  # 設置字型和大小
            draw.text((image.width - 200, image.height - 80), "@puffsdaily1216", fill=(255, 255, 255, 200), font=font)
            image = Image.alpha_composite(image, watermark)

            # Save compressed and watermarked image to original path
            directory, filename = os.path.split(image_path)
            compressed_filename = f"compressed_{filename}"
            compressed_image_path = os.path.join(directory, compressed_filename)

            # Convert image to RGB format to remove Alpha channel
            image = image.convert('RGB')

            # Save the image as JPEG format without optimization
            image.save(compressed_image_path, format='JPEG', quality=95, optimize=True)

            print(f"圖片已壓縮並加上浮水印，存放於 {compressed_image_path}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) < 2:
        print("請輸入圖片路徑")
        sys.exit(1)

    image_path = sys.argv[1]

    if not os.path.exists(image_path):
        print("路徑不存在")
        sys.exit(1)
    
    if not os.path.isfile(image_path):
        print("檔案不存在")
        sys.exit(1)

    # Compress and add watermark
    print("開始壓縮...")
    compress_and_watermark_image(image_path)

if __name__ == '__main__':
    main()