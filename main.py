import torch

weights = "person_m/best.pt"
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model = torch.hub.load('Ultralytics/yolov5', 'custom',weights, device='cpu',force_reload=True,trust_repo=True)

if __name__ == "__main__":
    model('남자사람_7_남_05733.jpg')