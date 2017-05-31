import argparse
import numpy as np
import data_io
from data_io import input_type, load_data
import model_alogs


def parse_cmd(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-I",
                        "--input",
                        type=str,
                        default="",
                        help="input data src"
                        )
    parser.add_argument("-O",
                        "--output",
                        type=str,
                        default="output data src",
                        help="output data src"
                        )
    parser.add_argument("-A",
                        "--alog",
                        type=str,
                        default="",
                        help="method to handle data "
                        )

    parser.add_argument("-CLS"
                        "--cols",
                        type=str,
                        default="cols to handle",
                        help="cols to handle"
                        )

    parser.add_argument(
        "--range",
        type=str,
        default="",
        help="scale range"
    )

    parsed, unparsed = parser.parse_known_args()
    para_dict = unparsed
    return parsed.input, parsed.output, parsed.alog, parsed.cols, para_dict


def get_input_x_y(input_data):
    x = np.array([[1, 3, 4], [2, 5, 6], [2, 5, 6]])
    y = np.array([1, 1])
    return x, y


def exec_cmd(input_data, output_data, alog_code, para_dict):
    if alog_code not in model_alogs.FUNC_DICT:
        raise Exception("not found alog named " % alog_code)
    input_x, input_y = get_input_x_y(input_data)
    if alog_code in model_alogs.MODLES:
        alog = model_alogs.FUNC_DICT[alog_code](para_dict, input_x, input_y)
        model_path = para_dict['model_path']
        data_io.save_model(alog, model_path)
    else:
        out_data, out_alog = model_alogs.FUNC_DICT[alog_code](para_dict, input_x, input_y)
        out_name = para_dict['output']
        data_io.save_csv_data(out_name)
        data_io.save_model(out_alog, "out_pre_pks/")


def main(args):
    input_table, out_table, trans_cols, method, paras = parse_cmd(args)
    input_data = load_data(input_table, input_type.CSV)


def test():
    data = load_data("test", input_type.CSV)


if __name__ == "__main__":
    '''
    python cmd.py -
    '''
    parser = argparse.ArgumentParser()
    parser.parse_args()
    main()
