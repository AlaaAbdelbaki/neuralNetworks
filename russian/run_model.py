import torch

# Load the model
model = torch.load('models/rnnGeneration_8_256.pt')

model.eval()
