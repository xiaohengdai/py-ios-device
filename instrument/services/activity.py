import time

from instrument.RPC import pre_call, get_usb_rpc


def activity(rpc, pid):
    def on_callback_message(res):
        print("[ACTIVITY]", res.parsed)
        print("\n")

    pre_call(rpc)
    rpc.register_channel_callback("com.apple.instruments.server.services.activity", on_callback_message)

    print("start", rpc.call("com.apple.instruments.server.services.activity", "startSamplingWithPid:", pid).parsed)

    try:
        while 1: time.sleep(10)
    except:
        pass
    print("stop", rpc.call("com.apple.instruments.server.services.activity", "stopSampling").parsed)
    rpc.stop()


if __name__ == '__main__':
    rpc = get_usb_rpc()
    activity(rpc,1519)
    rpc.deinit()
