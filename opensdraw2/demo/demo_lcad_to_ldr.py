import os
from opensdraw2.LegoModel import LegoModel
from opensdraw2.Generators.LdrGenerator import LcadGenerator


def load_model_from_lcad_file(file_name):
    return LegoModel(file_name)


def save_model_to_ldr_file(model, file_name):
    with open(file_name, 'w') as outfile_id:
        outfile_id.write(repr(LcadGenerator(model)))


if __name__ == "__main__":
    model = load_model_from_lcad_file(os.path.join('demo_models', "4x2brick.lcad2"))
    save_model_to_ldr_file(model, 'out.ldr')

    model = load_model_from_lcad_file(os.path.join('demo_models', "brick_house.lcad2"))
    save_model_to_ldr_file(model, 'brick_house.ldr')
