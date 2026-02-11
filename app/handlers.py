from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.requests as rq

router = Router()


class UserData(StatesGroup):
    age = State()
    gender = State()
    health_rate = State() #Как бы вы оценили свое общее физическое здоровье?
    hours_sleep = State() #Сколько часов в среднем вы спите каждую ночь?
    hard_to_sleep = State() #Вы испытываете трудности с засыпанием?
    often_wakeup = State() #Часто ли вы просыпаетесь ночью и долго не можете снова заснуть?
    time_sleep = State() #Во сколько вы обычно ложитесь спать в будние дни?
    trouble_to_sleep = State() #Что чаще всего мешает вам вовремя уснуть?
    tired_morning = State() #Чувствуете ли вы себя уставшим утром после пробуждения?
    bad_mood = State() #Замечали ли вы ухудшение настроения после плохого сна?
    angry_mood = State() #Испытываете ли вы раздражительность или агрессивность, когда плохо спите?
    easier_tasks = State() #Легче ли вам справляться с повседневными делами, когда вы хорошо отдохнули?
    headaches = State() #Возникают ли у вас головные боли или мигрень после бессонной ночи?
    anxiety = State() #Повышается ли уровень вашего беспокойства или тревожности при недостатке сна?
    less_concentration = State() #Замечали ли вы снижение концентрации, внимания и памяти при дефиците сна?
    trouble_education = State() #Сталкиваетесь ли вы с проблемами в учебе или социальной жизни вследствие нехватки сна?
    miss_lessons = State() #Приходилось ли вам пропускать занятия или важные дела из-за чувства усталости после плохого сна?
    satisfied_sleep = State() #Насколько вы удовлетворены качеством своего сна?
    often_dreams = State() #Как часто снятся вам сны?
    color_dreams = State() #Какого цвета ваши сны?




@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await rq.set_user(message.from_user.id)
    await state.set_state(UserData.age)
    await message.answer('''Приветствуем вас в SleepMindBot 🌙
                            
Дисклеймер:
Данный опрос является частью школьного исследовательского проекта и не является медицинской или клинической диагностикой.
Полученные результаты используются только в обобщённом виде для анализа влияния сна на психологическое состояние подростков.

Опрос анонимный. Личные данные не собираются.
Пожалуйста, отвечайте так, как это обычно бывает в вашей жизни, не выбирая «лучшие» ответы.

Для начала выберите ваш возраст.''', reply_markup=kb.age)
    

@router.callback_query(UserData.age, F.data.startswith('age_'))
async def question_age(callback: CallbackQuery, state: FSMContext):
    await state.update_data(age=callback.data.split('_')[1])
    await state.set_state(UserData.gender)
    await callback.message.edit_text('Выберите ваш пол.', reply_markup=kb.gender)


@router.callback_query(UserData.gender, F.data.startswith('gender_'))
async def question_fst(callback: CallbackQuery, state: FSMContext):
    await state.update_data(gender=callback.data.split('_')[1])
    await state.set_state(UserData.health_rate)
    await callback.message.edit_text('Вопрос 1. Как бы вы оценили свое общее физическое здоровье?', reply_markup=kb.health_rate)
    
    
@router.callback_query(UserData.health_rate, F.data.startswith('rate_'))
async def question_snd(callback: CallbackQuery, state: FSMContext):
    await state.update_data(health_rate=callback.data.split('_')[1])
    await state.set_state(UserData.hours_sleep)
    await callback.message.edit_text('Вопрос 2. Сколько часов в среднем вы спите каждую ночь?', reply_markup=kb.hours_sleep)
    
    
@router.callback_query(UserData.hours_sleep, F.data.startswith('hours_'))
async def question_thrd(callback: CallbackQuery, state: FSMContext):
    await state.update_data(hours_sleep=callback.data.split('_')[1])
    await state.set_state(UserData.hard_to_sleep)
    await callback.message.edit_text('Вопрос 3. Вы испытываете трудности с засыпанием?', reply_markup=kb.hard_to_sleep)

    
@router.callback_query(UserData.hard_to_sleep, F.data.startswith('hard_'))
async def question_frth(callback: CallbackQuery, state: FSMContext):
    await state.update_data(hard_to_sleep=callback.data.split('_')[1])
    await state.set_state(UserData.often_wakeup)
    await callback.message.edit_text('Вопрос 4. Часто ли вы просыпаетесь ночью и долго не можете снова заснуть?', reply_markup=kb.often_wakeup)
    
    
@router.callback_query(UserData.often_wakeup, F.data.startswith('wakeup_'))
async def question_ffth(callback: CallbackQuery, state: FSMContext):
    await state.update_data(often_wakeup=callback.data.split('_')[1])
    await state.set_state(UserData.time_sleep)
    await callback.message.edit_text('Вопрос 5. Во сколько вы обычно ложитесь спать в будние дни?', reply_markup=kb.time_sleep)
 

@router.callback_query(UserData.time_sleep, F.data.startswith('time_'))
async def question_sxth(callback: CallbackQuery, state: FSMContext):
    #key = callback.data.replace('time_', '')
    await state.update_data(time_sleep=kb.time_sleep_map.get(callback.data.split('_')[1]))
    await state.set_state(UserData.trouble_to_sleep)
    await callback.message.edit_text('Вопрос 6. Что чаще всего мешает вам вовремя уснуть?', reply_markup=kb.trouble_to_sleep)


@router.callback_query(UserData.trouble_to_sleep, F.data.startswith('trouble_'))
async def question_snth(callback: CallbackQuery, state: FSMContext):
    #key = callback.data.replace('trouble_', '')
    await state.update_data(trouble_to_sleep=kb.trouble_to_sleep_map.get(callback.data.split('_')[1]))
    await state.set_state(UserData.tired_morning)
    await callback.message.edit_text('Вопрос 7. Чувствуете ли вы себя уставшим утром после пробуждения?', reply_markup=kb.tired_morning)


@router.callback_query(UserData.tired_morning, F.data.startswith('tired_'))
async def question_etth(callback: CallbackQuery, state: FSMContext):
    await state.update_data(tired_morning=callback.data.split('_')[1])
    await state.set_state(UserData.bad_mood)
    await callback.message.edit_text('Вопрос 8. Замечали ли вы ухудшение настроения после плохого сна?', reply_markup=kb.bad_mood)


@router.callback_query(UserData.bad_mood, F.data.startswith('mood_'))
async def question_nnth(callback: CallbackQuery, state: FSMContext):
    await state.update_data(bad_mood=kb.bad_mood_map.get(callback.data.split('_')[1]))
    await state.set_state(UserData.angry_mood)
    await callback.message.edit_text('Вопрос 9. Испытываете ли вы раздражительность или агрессивность, когда плохо спите?', reply_markup=kb.angry_mood)


@router.callback_query(UserData.angry_mood, F.data.startswith('angry_'))
async def question_tnth(callback: CallbackQuery, state: FSMContext):
    await state.update_data(angry_mood=kb.angry_mood_map.get(callback.data.split('_')[1]))
    await state.set_state(UserData.easier_tasks)
    await callback.message.edit_text('Вопрос 10. Легче ли вам справляться с повседневными делами, когда вы хорошо отдохнули?', reply_markup=kb.easier_tasks)


@router.callback_query(UserData.easier_tasks, F.data.startswith('easier_'))
async def question_elth(callback: CallbackQuery, state: FSMContext):
    await state.update_data(easier_tasks=callback.data.split('_')[1])
    await state.set_state(UserData.headaches)
    await callback.message.edit_text('Вопрос 11. Возникают ли у вас головные боли или мигрень после бессонной ночи?', reply_markup=kb.headaches)


@router.callback_query(UserData.headaches, F.data.startswith('headaches_'))
async def question_twlth(callback: CallbackQuery, state: FSMContext):
    await state.update_data(headaches=callback.data.split('_')[1])
    await state.set_state(UserData.anxiety)
    await callback.message.edit_text('Вопрос 12. Повышается ли уровень вашего беспокойства или тревожности при недостатке сна?', reply_markup=kb.anxiety)


@router.callback_query(UserData.anxiety, F.data.startswith('anxiety_'))
async def question_thrn(callback: CallbackQuery, state: FSMContext):
    await state.update_data(anxiety=callback.data.split('_')[1])
    await state.set_state(UserData.less_concentration)
    await callback.message.edit_text('Вопрос 13. Замечали ли вы снижение концентрации, внимания и памяти при дефиците сна?', reply_markup=kb.less_concentration)


@router.callback_query(UserData.less_concentration, F.data.startswith('less_'))
async def question_frn(callback: CallbackQuery, state: FSMContext):
    await state.update_data(less_concentration=kb.less_concentration_map.get(callback.data.split('_')[1]))
    await state.set_state(UserData.trouble_education)
    await callback.message.edit_text('Вопрос 14. Сталкиваетесь ли вы с проблемами в учебе или социальной жизни вследствие нехватки сна?', reply_markup=kb.trouble_education)


@router.callback_query(UserData.trouble_education, F.data.startswith('education_'))
async def question_ffn(callback: CallbackQuery, state: FSMContext):
    await state.update_data(trouble_education=callback.data.split('_')[1])
    await state.set_state(UserData.miss_lessons)
    await callback.message.edit_text('Вопрос 15. Приходилось ли вам пропускать занятия или важные дела из-за чувства усталости после плохого сна?', reply_markup=kb.miss_lessons)


@router.callback_query(UserData.miss_lessons, F.data.startswith('miss_'))
async def question_sxn(callback: CallbackQuery, state: FSMContext):
    await state.update_data(miss_lessons=callback.data.split('_')[1])
    await state.set_state(UserData.satisfied_sleep)
    await callback.message.edit_text('Вопрос 16. Насколько вы удовлетворены качеством своего сна?', reply_markup=kb.satisfied)


@router.callback_query(UserData.satisfied_sleep, F.data.startswith('satisfied_'))
async def question_snn(callback: CallbackQuery, state: FSMContext):
    await state.update_data(satisfied_sleep=kb.satisfied_map.get(callback.data.split('_')[1]))
    await state.set_state(UserData.often_dreams)
    await callback.message.edit_text('Вопрос 17. Как часто снятся вам сны?', reply_markup=kb.often_dreams)


@router.callback_query(UserData.often_dreams, F.data.startswith('dreams_'))
async def question_etn(callback: CallbackQuery, state: FSMContext):
    await state.update_data(often_dreams=callback.data.split('_')[1])
    await state.set_state(UserData.color_dreams)
    await callback.message.edit_text('Вопрос 18. Какого цвета ваши сны?', reply_markup=kb.color_dreams)


@router.callback_query(UserData.color_dreams, F.data.startswith('color_'))
async def final(callback: CallbackQuery, state: FSMContext):
    await state.update_data(color_dreams=callback.data.split('_')[1])
    data = await state.get_data()
    await rq.add_data(data)
    await callback.message.edit_text('Благодарим вас за прохождение опроса!')
    await state.clear()





