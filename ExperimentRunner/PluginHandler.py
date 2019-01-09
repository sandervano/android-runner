import logging
import paths
import os
from pluginbase import PluginBase
from util import makedirs


class PluginHandler(object):
    def __init__(self, name, params):
        self.logger = logging.getLogger(self.__class__.__name__)

        self.nameLower = name.lower()
        self.moduleName = self.nameLower.capitalize()

        self.plugin_base = PluginBase(package='ExperimentRunner.plugins')
        if self.nameLower == 'android' or self.nameLower == 'trepn' or self.nameLower == 'batterystats':
            self.defaultPluginsPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Plugins')
            self.plugin_source = self.plugin_base.make_plugin_source(searchpath=[self.defaultPluginsPath])
        else:
            self.pluginPath = os.path.join(paths.CONFIG_DIR, 'Plugins')
            self.plugin_source = self.plugin_base.make_plugin_source(searchpath=[self.pluginPath])

        self.pluginModule = self.plugin_source.load_plugin(self.moduleName)
        self.paths = paths.paths_dict()
        self.currentProfiler = getattr(self.pluginModule, self.moduleName)(params, self.paths)
        self.logger.debug('%s: Initialized' % self.moduleName)

    def dependencies(self):
        return self.currentProfiler.dependencies()

    def load(self, device):
        """Load (and start) the profiler process on the device"""
        self.logger.debug('%s: %s: Loading configuration' % (self.moduleName, device))
        self.currentProfiler.load(device)

    def start_profiling(self, device, **kwargs):
        """Start the profiling process"""
        self.logger.debug('%s: %s: Start profiling' % (self.moduleName, device))
        self.currentProfiler.start_profiling(device, **kwargs)

    def stop_profiling(self, device, **kwargs):
        """Stop the profiling process"""
        self.logger.debug('%s: %s: Stop profiling' % (self.moduleName, device))
        self.currentProfiler.stop_profiling(device, **kwargs)

    def collect_results(self, device, path=None):
        """Collect the data and clean up extra files on the device"""
        self.logger.debug('%s: %s: Collecting data' % (self.moduleName, device))
        self.currentProfiler.collect_results(device, path)

    def unload(self, device):
        """Stop the profiler, removing configuration files on device"""
        self.logger.debug('%s: %s: Cleanup' % (self.moduleName, device))
        self.currentProfiler.unload(device)

    def set_output(self):
        self.paths['OUTPUT_DIR'] = os.path.join(paths.OUTPUT_DIR, self.nameLower + '/')
        makedirs(self.paths['OUTPUT_DIR'])
        self.currentProfiler.set_output(self.paths['OUTPUT_DIR'])

