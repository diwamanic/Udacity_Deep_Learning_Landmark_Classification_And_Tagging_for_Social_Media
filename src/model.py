import torch
import torch.nn as nn


# define the CNN architecture
class MyModel(nn.Module):
    def __init__(self, num_classes: int = 1000, dropout: float = 0.7) -> None:

        super().__init__()

        # YOUR CODE HERE
        # Define a CNN architecture. Remember to use the variable num_classes
        # to size appropriately the output of your classifier, and if you use
        # the Dropout layer, use the variable "dropout" to indicate how much
        # to use (like nn.Dropout(p=dropout))
        
        self.model = nn.Sequential(
            
            nn.Conv2d(3, 16, 3, padding=1),
            nn.MaxPool2d(2,2),
            nn.BatchNorm2d(16),
            nn.LeakyReLU(negative_slope=0.01),
            #nn.Dropout2d(p=dropout),
            
            nn.Conv2d(16, 32, 3, padding=1),
            nn.MaxPool2d(2,2),
            nn.BatchNorm2d(32),
            nn.LeakyReLU(negative_slope=0.01),
            #nn.Dropout2d(p=dropout),

            nn.Conv2d(32, 64, 3, padding=1),
            nn.MaxPool2d(2,2),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(negative_slope=0.01),
            #nn.Dropout2d(p=dropout),

            nn.Conv2d(64, 128, 3, padding=1),
            nn.MaxPool2d(2,2),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(negative_slope=0.01),
            #nn.Dropout2d(p=dropout),

            nn.Conv2d(128, 256, 3, padding=1),
            nn.MaxPool2d(2,2),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(negative_slope=0.01),
            nn.Dropout2d(p=dropout),

            nn.Flatten(),

            nn.BatchNorm1d(12544),
            nn.Linear(12544,256),
            nn.BatchNorm1d(256),
            nn.LeakyReLU(negative_slope=0.01),
            nn.Dropout(p=dropout),
            nn.Linear(256,128),
            nn.BatchNorm1d(128),
            nn.LeakyReLU(negative_slope=0.01),
            nn.Dropout(p=dropout),
            nn.Linear(128, num_classes)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # YOUR CODE HERE: process the input tensor through the
        # feature extractor, the pooling and the final linear
        # layers (if appropriate for the architecture chosen)
        return self.model(x)


######################################################################################
#                                     TESTS
######################################################################################
import pytest


@pytest.fixture(scope="session")
def data_loaders():
    from .data import get_data_loaders

    return get_data_loaders(batch_size=2)


def test_model_construction(data_loaders):

    model = MyModel(num_classes=23, dropout=0.3)

    dataiter = iter(data_loaders["train"])
    images, labels = dataiter.next()

    out = model(images)

    assert isinstance(
        out, torch.Tensor
    ), "The output of the .forward method should be a Tensor of size ([batch_size], [n_classes])"

    assert out.shape == torch.Size(
        [2, 23]
    ), f"Expected an output tensor of size (2, 23), got {out.shape}"
