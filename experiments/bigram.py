import torch
from src.create_bigram_dataset import X_encoded, Y

# create the Weight matrices with random values

W = torch.randn((28, 28), requires_grad=True)
X = X_encoded

logits = X @ W



counts = torch.exp(logits)

probabilities = counts / counts.sum(dim=1, keepdim=True)

print(probabilities)
print(probabilities.sum())

print(probabilities.min())
print(probabilities.max())
print(probabilities.sum())

target = Y

probability_target = probabilities[torch.arange(len(Y)), target]


losses = -torch.log(probability_target)
loss = losses.mean()
print('loss', loss.item())

loss.backward()

print(W.grad.shape)
print(W.grad)

print(W.grad.min())
print(W.grad.max())
print(W.grad.mean())