from sqlalchemy import BigInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)

    #health_rate: Mapped[str] = mapped_column(String(8))
    #hours_of_sleep: Mapped[str] = mapped_column(String(5))

class Data(Base):
    __tablename__ = 'data'

    id: Mapped[int] = mapped_column(primary_key=True)

    Возраст: Mapped[str] = mapped_column(String(8))
    Пол: Mapped[str] = mapped_column(String(8))
    Как_бы_вы_оценили_свое_общее_физическое_здоровье: Mapped[str] = mapped_column(String(10))
    Сколько_часов_в_среднем_вы_спите_каждую_ночь: Mapped[str] = mapped_column(String(5))
    Вы_часто_испытываете_трудности_с_засыпанием: Mapped[str] = mapped_column(String(25))
    Часто_ли_вы_просыпаетесь_ночью_и_долго_не_можете_снова_заснуть: Mapped[str] = mapped_column(String(20))
    Во_сколько_вы_обычно_ложитесь_спать_в_будние_дни: Mapped[str] = mapped_column(String(35))
    Что_чаще_всего_мешает_вам_вовремя_уснуть: Mapped[str] = mapped_column(String(35))
    Чувствуете_ли_вы_себя_уставшим_утром_после_пробуждения: Mapped[str] = mapped_column(String(15))
    Замечали_ли_вы_ухудшение_настроения_после_плохого_сна: Mapped[str] = mapped_column(String(40))
    Испытываете_ли_вы_раздраженность_или_агрессивность_когда_плохо_спите: Mapped[str] = mapped_column(String(35))
    Легче_ли_вам_справляться_с_повседневными_делами_когда_вы_хорошо_отдохнули: Mapped[str] = mapped_column(String(20))
    Возникают_ли_у_вас_головные_боли_или_мигрень_после_бессонной_ночи: Mapped[str] = mapped_column(String(25))
    Повышается_ли_уровень_вашего_беспокойства_или_тревожности_при_недостатке_сна: Mapped[str] = mapped_column(String(30))
    Замечали_ли_вы_снижение_концентрации_внимания_и_памяти_при_дефиците_сна: Mapped[str] = mapped_column(String(60))
    Сталкивались_ли_вы_с_проблемами_в_учебе_или_социальной_жизни_вследствие_нехватки_сна: Mapped[str] = mapped_column(String(35))
    Приходилось_ли_вам_пропускать_занятия_или_важные_дела_изза_чувства_усталости_после_плохого_сна: Mapped[str] = mapped_column(String(25))
    Насколько_вы_удовлетворены_качеством_своего_сна: Mapped[str] = mapped_column(String(40))
    Как_часто_снятся_вам_сны: Mapped[str] = mapped_column(String(30))
    Какого_цвета_ваши_сны: Mapped[str] = mapped_column(String(35))



async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)