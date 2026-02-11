from app.database.models import async_session
from app.database.models import User, Data
from sqlalchemy import select


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()

async def add_data(data):
    async with async_session() as session:
        session.add(Data(Возраст=data["age"], Пол=data["gender"], Как_бы_вы_оценили_свое_общее_физическое_здоровье=data["health_rate"], Сколько_часов_в_среднем_вы_спите_каждую_ночь=data["hours_sleep"], Вы_часто_испытываете_трудности_с_засыпанием=data["hard_to_sleep"], Часто_ли_вы_просыпаетесь_ночью_и_долго_не_можете_снова_заснуть=data["often_wakeup"], Во_сколько_вы_обычно_ложитесь_спать_в_будние_дни=data["time_sleep"], Что_чаще_всего_мешает_вам_вовремя_уснуть=data["trouble_to_sleep"], Чувствуете_ли_вы_себя_уставшим_утром_после_пробуждения=data["tired_morning"], Замечали_ли_вы_ухудшение_настроения_после_плохого_сна=data["bad_mood"], Испытываете_ли_вы_раздраженность_или_агрессивность_когда_плохо_спите=data["angry_mood"], Легче_ли_вам_справляться_с_повседневными_делами_когда_вы_хорошо_отдохнули=data["easier_tasks"], Возникают_ли_у_вас_головные_боли_или_мигрень_после_бессонной_ночи=data["headaches"], Повышается_ли_уровень_вашего_беспокойства_или_тревожности_при_недостатке_сна=data["anxiety"], Замечали_ли_вы_снижение_концентрации_внимания_и_памяти_при_дефиците_сна=data["less_concentration"], Сталкивались_ли_вы_с_проблемами_в_учебе_или_социальной_жизни_вследствие_нехватки_сна=data["trouble_education"], Приходилось_ли_вам_пропускать_занятия_или_важные_дела_изза_чувства_усталости_после_плохого_сна=data["miss_lessons"], Насколько_вы_удовлетворены_качеством_своего_сна=data["satisfied_sleep"], Как_часто_снятся_вам_сны=data["often_dreams"], Какого_цвета_ваши_сны=data["color_dreams"]))
        await session.commit()