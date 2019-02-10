import logging
import paths
import inspect
import os
import time
import traceback
import Checks
from PluginHandler import PluginHandler
from Devices import Devices
from util import makedirs

class Tests(object):

    def __init__(self, config):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.errors = []
        self.config = config
        adb_path = config.get('adb_path', 'adb')
        self.devices = Devices(config['devices'], adb_path=adb_path)
        self.profilers = None
        self.output_root = paths.OUTPUT_DIR
        self.result_file = os.path.join(self.output_root, 'Test_results.txt')

    def get_progress_xml_file(self):
        return "Testing, no progress file has been made"

    def check_profilers(self):
        self.check_init_profilers()
        default_profilers = ['android', 'batterystats', 'trepn']
        for profiler in self.profilers:
            if profiler.nameLower not in default_profilers:
                self.check_profiler(profiler.currentProfiler, profiler.moduleName)

    def check_init_profilers(self):
        self.profilers = []
        for name, params in self.config.get('profilers', {}).items():
            try:
                self.profilers.append(PluginHandler(name, params))
            except Exception as e:
                self.errors.append('Profiler {}: Initializing profiler resulted in the following error:\n{}'.
                                   format(name, traceback.format_exc()))

    def check_profiler(self, profiler, profiler_name):
        profiler_parent = inspect.getmro(type(profiler))[1]
        profiler_parent_module = profiler_parent.__module__
        profiler_parent_name = profiler_parent.__name__
        if '.Profiler' in profiler_parent_module and profiler_parent_name == 'Profiler':
            self.check_profiler_methods(profiler, profiler_name)
        else:
            self.errors.append('Profiler {}: doesn\'t have the \'Profiler\' '
                               'as parent class, plugin can\'t be tested'.format(profiler_name))

    def check_profiler_methods(self, profiler, profiler_name):
        method = 'dependencies()'
        try:
            method_result = profiler.dependencies()
            self.check_dependencies(method_result, profiler_name)
        except NotImplementedError:
            self.errors.append('Profiler {}: Method {} not implemented.'.format(profiler_name, method))
        except Exception as e:
            self.errors.append('Profiler {}: Method {} gave the following error: \n{}'
                               .format(profiler_name, method, traceback.format_exc()))

        device = None
        try:
            for current_device in self.devices:
                installed_apps = current_device.is_installed(profiler.dependencies())
                not_installed_apps = [name for name, installed in installed_apps.items() if not installed]
                if len(not_installed_apps) == 0:
                    device = current_device
                    break
        finally:
            if device is None:
                self.errors.append('Profiler {}: plugin not further tested, '
                                   'no device available that meets the dependencies. '
                                   'Check devices and dependencies'.format(profiler_name))
                return

        method = 'load()'
        try:
            method_result = profiler.load(device)
            if method_result is not None:
                self.errors.append("Profiler {}: Method {} gives non expected return value.".
                                   format(profiler_name, method))
        except NotImplementedError:
            self.errors.append('Profiler {}: Method {} not implemented.'.format(profiler_name, method))
        except Exception as e:
            self.errors.append('Profiler {}: Method {} gave the following error: \n{}'
                               .format(profiler_name, method, traceback.format_exc()))

        method = 'set_output()'
        profiler_test_output = os.path.join(self.output_root, 'data',
                                            device.name, 'test_dir_1', 'test_dir_2', profiler_name.lower())
        try:
            method_result = profiler.set_output(profiler_test_output)
            if method_result is not None:
                self.errors.append("Profiler {}: Method {} gives non expected return value.".
                                   format(profiler_name, method))
        except NotImplementedError:
            self.errors.append('Profiler {}: Method {} not implemented.'.format(profiler_name, method))
        except Exception as e:
            self.errors.append('Profiler {}: Method {} gave the following error: \n{}'
                               .format(profiler_name, method, traceback.format_exc()))
        makedirs(profiler_test_output)

        method = 'start_profiling()'
        try:
            method_result = profiler.start_profiling(device)
            if method_result is not None:
                self.errors.append("Profiler {}: Method {} gives non expected return value.".
                                   format(profiler_name, method))
        except NotImplementedError:
            self.errors.append('Profiler {}: Method {} not implemented.'.format(profiler_name, method))
        except Exception as e:
            self.errors.append('Profiler {}: Method {} gave the following error: \n{}'
                               .format(profiler_name, method, traceback.format_exc()))

        """Ensures something is measured for testing"""
        time.sleep(5)

        method = 'stop_profiling()'
        try:
            method_result = profiler.stop_profiling(device)
            if method_result is not None:
                self.errors.append("Profiler {}: Method {} gives non expected return value.".
                                   format(profiler_name, method))
        except NotImplementedError:
            self.errors.append('Profiler {}: Method {} not implemented.'.format(profiler_name, method))
        except Exception as e:
            self.errors.append('Profiler {}: Method {} gave the following error: \n{}'
                               .format(profiler_name, method, traceback.format_exc()))

        """Gives time to end all multi threaded profiling"""
        time.sleep(5)

        method = 'collect_results()'
        try:
            method_result = profiler.collect_results(device)
            if method_result is not None:
                self.errors.append("Profiler {}: Method {} gives non expected return value.".
                                   format(profiler_name, method))
        except NotImplementedError:
            self.errors.append('Profiler {}: Method {} not implemented.'.format(profiler_name, method))
        except Exception as e:
            self.errors.append('Profiler {}: Method {} gave the following error: \n{}'
                               .format(profiler_name, method, traceback.format_exc()))

        method = 'aggregate_subject()'
        try:
            method_result = profiler.aggregate_subject()
            if method_result is not None:
                self.errors.append("Profiler {}: Method {} gives non expected return value.".
                                   format(profiler_name, method))
        except NotImplementedError:
            self.errors.append('Profiler {}: Method {} not implemented.'.format(profiler_name, method))
        except Exception as e:
            self.errors.append('Profiler {}: Method {} gave the following error: \n{}'
                               .format(profiler_name, method, traceback.format_exc()))

        method = 'unload()'
        try:
            method_result = profiler.unload(device)
            if method_result is not None:
                self.errors.append("Profiler {}: Method {} gives non expected return value.".
                                   format(profiler_name, method))
        except NotImplementedError:
            self.errors.append('Profiler {}: Method {} not implemented.'.format(profiler_name, method))
        except Exception as e:
            self.errors.append('Profiler {}: Method {} gave the following error: \n{}'
                               .format(profiler_name, method, traceback.format_exc()))

        method = 'aggregate_end()'
        try:
            method_result = profiler.aggregate_end(os.path.join(paths.OUTPUT_DIR, 'data'),
                                                   os.path.join(paths.OUTPUT_DIR, '{}_aggregated.csv').
                                                   format(profiler_name))
            if method_result is not None:
                self.errors.append("Profiler {}: Method {} gives non expected return value.".
                                   format(profiler_name, method))
        except NotImplementedError:
            self.errors.append('Profiler {}: Method {} not implemented.'.format(profiler_name, method))
        except Exception as e:
            self.errors.append('Profiler {}: Method {} gave the following error: \n{}'
                               .format(profiler_name, method, traceback.format_exc()))

    def check_dependencies(self, dependencies, profiler_name):
        if isinstance(dependencies, list):
            for dependency in dependencies:
                if isinstance(dependency, basestring):
                    if len(dependency.split(".")) == 3:
                        continue
                    else:
                        self.errors.append('Profiler {}: dependency \'{}\' has an invalid format'
                                           .format(profiler_name, dependency))
                else:
                    self.errors.append('Profiler {}: invalid object in dependency list'
                                       .format(profiler_name))
        else:
            self.errors.append('Profiler {}: return value of dependencies() not a list object'.format(profiler_name))

    def format_errors(self):
        result_string = ''
        if len(self.errors) > 0:
            result_string += '{} Errors found during testing: \n'.format(len(self.errors))
            for error in self.errors:
                result_string += '\n{}'.format(error)
        else:
            result_string += "No errors found during testing"
        return result_string

    def write_to_file(self, formatted_errors):
        with open(self.result_file, 'w') as f:
            f.write(formatted_errors)

    def start(self):
        self.check_profilers()
        formated_errors = self.format_errors()
        self.write_to_file(formated_errors)
        print '\n{}'.format(formated_errors)
        print '\nTest results saved to file: {}'.format(self.result_file)
