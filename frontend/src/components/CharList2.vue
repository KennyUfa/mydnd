<template>
  <div class="container  p-4">
    <div class="row mb-3">
      <div class="col-12 text-center">
        <h2>Список Навыков</h2>
      </div>
    </div>

    <div class="row">
      <!-- Сила -->
      <div class="col-4">
        <h5>СИЛА</h5>
        <div class="mb-2">Атлетика: +1</div>
      </div>

      <!-- Ловкость -->
      <div class="col-4">
        <h5>ЛОВКОСТЬ</h5>
        <div class="mb-2">Акробатика: +5</div>
        <div class="mb-2">Ловкость рук: +5</div>
        <div class="mb-2">Скрытность: +5</div>
      </div>

    </div>

    <div class="row mt-3">
      <!-- Интеллект -->
      <div class="col-4">
        <h5>ИНТЕЛЛЕКТ</h5>
        <div class="mb-2">Анализ: +5</div>
        <div class="mb-2">История: +8</div>
        <div class="mb-2">Магия: +5</div>
        <div class="mb-2">Природа: +3</div>
        <div class="mb-2">Религия: +5</div>
      </div>

      <!-- Мудрость -->
      <div class="col-4">
        <h5>МУДРОСТЬ</h5>
        <div class="mb-2">Восприятие: +4</div>
        <div class="mb-2">Выживание: +2</div>
        <div class="mb-2">Медицина: +2</div>
        <div class="mb-2">Проницательность: +4</div>
        <div class="mb-2">Уход за животными: +2</div>
      </div>

      <!-- Харизма -->
      <div class="col-4">
        <h5>ХАРИЗМА</h5>
        <div class="mb-2">Выступление: +5</div>
        <div class="mb-2">Запугивание: +5</div>
        <div class="mb-2">Обман: +7</div>
        <div class="mb-2">Убеждение: +10</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SkillList',
};
</script>

<style>
.container {
  max-width: 900px;
}
h5 {
  font-weight: bold;
  margin-bottom: 10px;
  text-decoration: underline;
}
.mb-2 {
  margin-bottom: 8px;
}
</style>
