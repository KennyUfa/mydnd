<script>
export default {
  name: "about"
}
</script>

<template>
  <main class="main">
    <div class="left_main">
      <h1>Егор Родионов</h1>
      <h2>Full-Stack Developer</h2>
    </div>
    <div class="profile-photo"></div>
  </main>
  <section class="about_me">
    <h2 class="about_me_title">Обо мне</h2>
    <div class="about_me_text">
      <p>Привет! Меня зовут Егор, и я начинающий fullstack-разработчик.</p>
      <p>Уже несколько месяцев изучаю веб-технологии и создаю небольшие проекты,
        чтобы применять знания на
        практике. Люблю
        решать задачи, учиться новому и стремлюсь стать частью дружной
        разработческой команды.</p>
      <p>Мне интересны обе стороны разработки — клиентская и серверная. Мои
        основные инструменты:</p>
      <ul>
        <li><strong>Frontend:</strong> HTML, CSS, JavaScript, Vue.js</li>
        <li><strong>Backend:</strong> Python, Django REST</li>
        <li><strong>Дополнительно:</strong> Git, REST API, SQL, C, Docker</li>
      </ul>
      <p>Сейчас я в поиске первой позиции junior-разработчика, где смогу
        развивать свои навыки и расти как
        специалист.</p>
      <p>Если вы ищете нового участника команды или просто хотите узнать больше
        обо мне — смело пишите!</p>
    </div>
  </section>
  <section class="portfolio">
    <h2 class="portfolio_title">Мои проекты и достижения</h2>
    <div class="projects">
      <div class="project_frame">
        <div class="title">Dungeon And Dragons Charlist</div>
        <div class="descr">Лист персонажа для игры в Днд. С базой знаний и
          системой рассчетов.<br/> <br/>Есть
          рабочая версия, продолжаю работать над улучшением
        </div>
      </div>
      <div class="project_frame">
        <div class="title">Личный сайт - резюме</div>
        <div class="descr">Создал личный сайт - резюме.</div>
      </div>
      <div class="project_frame">
        <div class="title">Школа 21</div>
        <div class="descr">Прошел большой конкурсный отбор и получил бесплатное
          обучение.
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="footer-info">
      © 2025 Егор Родионов. Возможно все права защищены.
      <div class="social-links" style="margin-top: 10px;">
        <a href="https://github.com/KennyUfa" target="_blank">GitHub</a>
        <a href="mailto:kennyufa444@gmail.com">Email</a>
      </div>
    </div>
  </footer>

</template>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Russo One", sans-serif;
  font-size: 16px;
  color: #1cba6b;
}

body {
  background: rgb(23, 23, 23);
  max-width: 1180px;
  margin: 0 auto;
  padding: 25px;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main,
.about_me,
.portfolio {
  flex: 1 0 auto;
}

.header {
  height: 80px;
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  background: rgb(23, 23, 23);
}

.menu {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.name {
  color: rgb(255, 255, 255);
  font-size: 2rem;
  font-weight: 700;
}

.nav {
  display: flex;
  gap: 32px;
}

.nav a {
  text-decoration: none;
  padding: 6px 16px;
  border-radius: 6px;
  transition: background 0.2s, color 0.2s;
}

.nav a:hover {
  background: #373a3f;
  color: #1cba6b;
}

/* ================================ main ================================ */

.main {
  max-height: 500px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-size: cover;
  margin-top: 50px;
  padding: 0 20px;
}

.left_main p {
  font-size: 1.4rem;
  margin-bottom: 10px;
}


.left_main h1 {
  font-size: 3rem;
  margin-bottom: 15px;
  background-clip: content-box;
  background: linear-gradient(45deg, #1cba6b 30%, #ffffff 70%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.left_main h2 {
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
  background-clip: content-box;
  background: linear-gradient(45deg, #1cba6b 30%, #ffffff 70%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.profile-photo {
  min-width: 350px;
  min-height: 350px;
  background-size: 135%;
  background-position: center;
  border-radius: 50%;
  border: 1px solid rgb(0, 252, 67, 0.6);
  background-image:
    url('@/assets/tRD7lCyffcZFn9o6nvYgLZ1WWLeRycfc8Vl4RoesIp4wlCsS5AYyQuPjcC-Qg2CGA4j901G6.jpg');
  box-shadow: 15px -20px 50px 20px rgba(0, 252, 67, 0.8);
  animation: float 3s ease-in-out infinite;
}


@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-10px);
  }
}


/* ============ about ============ */


.about_me {
  background: #205c2d;
  border-radius: 24px;
  padding: 24px;
  box-shadow: 0 0 15px rgba(28, 250, 95, 0.1);
  margin-top: 50px;
}

.about_me:hover {
  transform: translateY(-5px);
}

.about_me_title {
  font-size: 48px;
  font-weight: 700;
  text-align: center;
  margin-bottom: 18px;
  color: white;
}

.about_me_text p, li, strong {
  color: #ccc;
  font-size: 18px;
  font-weight: 400;
  line-height: 1.8;
}

.about_me_text ul {
  margin: 10px 0;
  list-style: none;
  color: #1cba6b;
}

/* ======= portfolio ======= */

.portfolio {
  margin-top: 30px;
}

.portfolio_title {
  font-size: 48px;
  font-weight: 700;
  text-align: center;
  margin-bottom: 30px;
  color: white;
}

.projects {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}


.project_frame {
  background: #205c2d;;
  padding: 25px;
  flex: 1 1 270px;
  border-radius: 12px;
  box-shadow: 0 0 15px rgba(28, 250, 95, 0.1);
  transition: transform 0.3s ease;
}

.project_frame:hover {
  transform: translateY(-5px);
}

.project_frame .title {
  font-size: 20px;
  font-weight: 700;
  text-align: center;
  color: white;
}

.project_frame .descr {
  font-weight: 300;
  text-align: left;
  margin-top: 30px;
}

/* ======= footer ======= */
.footer {
  width: 100%;
  padding-top: 30px;
  text-align: center;
  color: #888;
  font-size: 14px;
  margin-top: auto;
  margin-bottom: 30px;
}

.footer a {
  color: #1cba6b;
  text-decoration: none;
  margin-left: 10px;
}

.footer a:hover {
  text-decoration: underline;
}

@media (max-width: 768px) {
  .main {
    flex-direction: column;
    align-items: center;
  }

  .profile-photo {
    min-width: 200px;
    min-height: 200px;
  }

  .left_main {
    width: 100%;
    text-align: center;
  }

  .profile-photo {
    width: 250px;
    height: 250px;
    margin-top: 50px;
  }

  .about_me {
    margin-top: 50px;
  }

}
</style>