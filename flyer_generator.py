from PIL import Image, ImageDraw, ImageFont
import random
import os
from datetime import datetime

def create_flyer():
    # Create output folder
    output_folder = "flyer_output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Colors and content
    colors = [
        (70, 130, 180),   # Steel Blue
        (220, 20, 60),    # Crimson
        (46, 139, 87),    # Sea Green
        (255, 140, 0),    # Dark Orange
        (147, 112, 219)   # Medium Purple
    ]
    
    titles = ["Summer Sale", "Grand Opening", "Special Event", "Workshop", "Concert", "Festival", "Open House"]
    descriptions = [
        "Don't miss our amazing event!",
        "Join us for fun and learning!",
        "Limited time offer!",
        "Exciting things are happening!",
        "Live music and great food!",
        "Free entry for everyone!",
        "Special guest appearances!"
    ]

    # Create image
    width, height = 800, 1200
    bg_color = random.choice(colors)
    image = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(image)

    # Try to use fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 60)
        desc_font = ImageFont.truetype("arial.ttf", 30)
    except:
        title_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()

    # Add content
    title = random.choice(titles)
    description = random.choice(descriptions)
    
    # Draw elements
    draw.text((100, 100), title, fill=(255, 255, 255), font=title_font)
    draw.text((100, 200), description, fill=(255, 255, 255), font=desc_font)
    draw.text((100, 300), f"Date: {random.choice(['Saturday', 'Sunday'])}", fill=(255, 255, 255), font=desc_font)
    draw.text((100, 350), f"Time: {random.choice(['2:00 PM', '6:00 PM', '10:00 AM'])}", fill=(255, 255, 255), font=desc_font)
    draw.text((100, 400), f"Location: {random.choice(['Central Park', 'Main Street', 'City Hall'])}", fill=(255, 255, 255), font=desc_font)

    # Save
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"{output_folder}/flyer_{timestamp}.png"
    image.save(filename)
    return filename

# Create multiple flyers
print("Creating random flyers...")
for i in range(5):
    filename = create_flyer()
    print(f"Created: {filename}")

print(f"\nAll flyers saved in: {os.path.abspath('flyer_output')}")
print("You can find your flyers in the 'flyer_output' folder!")