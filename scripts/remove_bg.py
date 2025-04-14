from PIL import Image
from rembg import remove

# 加载图像并去除背景
with open("/data/cxy/Github/videovista-culturallingo.github.io/static/images/videovista.png", "rb") as i:
    input_image = i.read()
    output_image = remove(input_image)

# 保存透明背景图
with open("/data/cxy/Github/videovista-culturallingo.github.io/static/images/no_bg.png", "wb") as o:
    o.write(output_image)

# 加载透明图像
image = Image.open("/data/cxy/Github/videovista-culturallingo.github.io/static/images/no_bg.png").convert("RGBA")

# 创建新背景色图层
background = Image.new("RGBA", image.size, (255, 255, 0, 255))  # 黄色背景

# 合成图像
composite = Image.alpha_composite(background, image)

# 保存结果
composite.convert("RGB").save("/data/cxy/Github/videovista-culturallingo.github.io/static/images/videovista_new.png")
