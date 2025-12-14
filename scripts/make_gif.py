import os
import glob
from ase.io import read, write
from PIL import Image  # 파이썬 기본 이미지 라이브러리 (Pillow)

# ==========================================
# [설정] 파일 이름 확인!
filename = 'LiFePO4.cif' 
output_gif = 'LiFePO4_spin.gif'
# ==========================================

# 1. CIF 파일 불러오기
if not os.path.exists(filename):
    print(f"❌ '{filename}' 파일이 없습니다. 파일명을 확인해주세요!")
    exit()

print(f"✅ '{filename}' 로드 성공! 이미지 렌더링을 시작합니다...")
structure = read(filename)

# 2. 임시 폴더 만들기 (사진 60장 저장용)
temp_dir = 'temp_frames'
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# 3. 한 장씩 돌려가며 PNG로 저장 (ASE는 PNG 저장을 아주 잘함)
n_frames = 60
print("📸 찰칵찰칵 촬영 중 (0/60)...")

for i in range(n_frames):
    # 회전 (Y축 기준)
    structure.rotate(360 / n_frames, 'y')
    
    # PNG로 저장 (temp_frames/frame_000.png 형식)
    # rotation='-10z,-70x' 등으로 보는 각도를 예쁘게 조정 가능
    # ASE의 write 함수는 PNG 저장 시 에러가 거의 없음
    write(f'{temp_dir}/frame_{i:03d}.png', structure)
    
    if i % 10 == 0:
        print(f"   ... {i}장 완료")

print("📸 촬영 끝! GIF로 조립합니다...")

# 4. PNG들을 불러와서 GIF로 묶기 (Pillow 사용 - FFMPEG 필요 없음)
# 저장된 순서대로 파일 리스트 가져오기
files = sorted(glob.glob(f'{temp_dir}/frame_*.png'))

if not files:
    print("❌ 에러: 생성된 이미지가 없습니다.")
    exit()

# 이미지 객체로 변환
images = [Image.open(f) for f in files]

# GIF 저장
# loop=0 은 무한반복, duration은 프레임당 시간(ms)
images[0].save(
    output_gif,
    save_all=True,
    append_images=images[1:],
    duration=100, 
    loop=0        
)

# 5. 뒷정리 (임시 PNG 파일 삭제)
print("🧹 청소 중...")
for f in files:
    os.remove(f)
os.rmdir(temp_dir)

print(f"🎉 완전 성공! '{output_gif}' 파일을 확인하세요!")
