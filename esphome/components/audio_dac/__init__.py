import esphome.codegen as cg
import esphome.config_validation as cv

CODEOWNERS = ["@formatBCE"]
MULTI_CONF = True


audio_dac_ns = cg.esphome_ns.namespace("audio_dac")
AudioDac = audio_dac_ns.class_("AudioDac", cg.Component)

AUDIO_DAC_SCHEMA = cv.Schema({})

PLATFORM_SCHEMA = AUDIO_DAC_SCHEMA
CONFIG_SCHEMA = cv.ensure_list(PLATFORM_SCHEMA)


async def register_audio_dac(var, config):
    return
