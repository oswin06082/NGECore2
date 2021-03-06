import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from java.util import Vector


def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('dark_jedi_knight')
	mobileTemplate.setLevel(90)
	mobileTemplate.setMinLevel(62)
	mobileTemplate.setMaxLevel(70)
	mobileTemplate.setDifficulty(Difficulty.ELITE)

	mobileTemplate.setMinSpawnDistance(3)
	mobileTemplate.setMaxSpawnDistance(5)
	mobileTemplate.setDeathblow(True)
	mobileTemplate.setSocialGroup('dark jedi')
	mobileTemplate.setAssistRange(12)
	mobileTemplate.setRespawnTime(300)
	mobileTemplate.setOptionsBitmask(Options.AGGRESSIVE | Options.ATTACKABLE)
	
	templates = Vector()
	templates.add('object/mobile/shared_dressed_dark_jedi_male_human_01.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_male_human_02.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_male_human_03.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_male_human_04.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_male_human_05.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_male_human_06.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_male_twk_01.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_male_twk_02.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_male_twk_03.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_male_zab_01.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_male_zab_02.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_male_zab_03.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_female_human_01.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_female_human_02.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_female_human_03.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_female_human_04.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_female_twk_01.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_female_twk_02.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_female_twk_03.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_female_zab_01.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_female_zab_02.iff')
	templates.add('object/mobile/shared_dressed_dark_jedi_female_zab_03.iff')
	
	
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/sword/crafted_saber/shared_sword_lightsaber_one_handed_gen5.iff', WeaponType.ONEHANDEDSABER, 1.0, 6, 'energy')
	weaponTemplates.add(weapontemplate)
	weapontemplate = WeaponTemplate('object/weapon/melee/2h_sword/crafted_saber/shared_sword_lightsaber_two_handed_gen5.iff', WeaponType.TWOHANDEDSABER, 1.0, 6, 'energy')
	weaponTemplates.add(weapontemplate)
	weapontemplate = WeaponTemplate('object/weapon/melee/polearm/crafted_saber/shared_sword_lightsaber_polearm_gen5.iff', WeaponType.POLEARMSABER, 1.0, 6, 'energy')
	weaponTemplates.add(weapontemplate)	
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('saberHit')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('dark_jedi_knight', mobileTemplate)
	