import os.path as op
import time

import Tests
from Experiment import Experiment
from util import ConfigError


class NativeExperiment(Experiment):
    def __init__(self, config, progress):
        self.package = None
        self.duration = Tests.is_integer(config.get('duration', 0)) / 1000
        super(NativeExperiment, self).__init__(config, progress)
        for apk in config.get('paths', []):
            if not op.isfile(apk):
                raise ConfigError('File %s not found' % apk)

    def cleanup(self, device):
        super(NativeExperiment, self).cleanup(device)
        if self.package in device.get_app_list():
            device.uninstall(self.package)

    def before_experiment(self, device, *args, **kwargs):
        super(NativeExperiment, self).before_experiment(device)

    def before_run_subject(self, device, path, *args, **kwargs):
        super(NativeExperiment, self).before_run_subject(device, path)
        filename = op.basename(path)
        self.logger.info('APK: %s' % filename)
        if filename not in device.get_app_list():
            device.install(path)
        self.package = op.splitext(op.basename(path))[0]

    def before_run(self, device, path, run, *args, **kwargs):
        super(NativeExperiment, self).before_run(device, path, run)
        device.launch_package(self.package)
        self.after_launch(device, path, run)

    def start_profiling(self, device, path, run, *args, **kwargs):
        self.profilers.start_profiling(device, app=self.package)
        time.sleep(self.duration)

    def after_run(self, device, path, run, *args, **kwargs):
        self.before_close(device, path, run)
        device.force_stop(self.package)
        super(NativeExperiment, self).after_run(device, path, run)

    def after_last_run(self, device, path, *args, **kwargs):
        super(NativeExperiment, self).after_last_run(device, path)
        device.uninstall(self.package)
        self.package = None

    def after_experiment(self, device, *args, **kwargs):
        super(NativeExperiment, self).after_experiment(device)
