<script>
  import { userIsLogged } from "$lib/user.js";
  import { page } from "$app/stores";

  const slug = $page.params.slug;
  let currentPage = 1;
  let pageLimit = 10;
  const isLogged = userIsLogged();
  const pageLimits = [
    { value: 10, label: "10개씩 보기" },
    { value: 15, label: "15개씩 보기" },
    { value: 20, label: "20개씩 보기" },
  ];
  let currentLimit = pageLimits[0].value;

  const getSlugList = async (slug, pageIdx, pageLimit) => {
    const res = await fetch(
      `//api.eyo.kr/board/qna/list/slug/${slug}/${pageIdx}?limit=${pageLimit}`,
      {
        mode: "cors",
        credentials: "include",
      }
    ).catch((err) => {
      console.log(err);
    });
    const slugBoard = await res.json();
    if (res.ok) {
      return slugBoard;
    } else {
      throw new Error(slugBoard);
    }
  };
  $: slugList = getSlugList(slug, currentPage, pageLimit);

  const getName = async (slug) => {
    const res = await fetch(
      `//api.eyo.kr/board/tag/get_name_by_slug/${slug}`,
      {
        mode: "cors",
        credentials: "include",
      }
    ).catch((err) => {
      console.log(err);
    });
    const tagName = await res.json();
    if (res.ok) {
      return tagName;
    } else {
      throw new Error(tagName);
    }
  };
  $: tagName = getName(slug);
</script>

{#await tagName then slugName}
  <header>
    <section class="hero is-small ">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">{slugName}</h1>
        </div>
      </div>
    </section>
  </header>
{/await}

<div class="container">
  <table
    class="table container is-fluid has-text-centered"
    style="margin-bottom: 0;"
  >
    <thead>
      <tr>
        <th class="has-text-centered">제목</th>
        <th class="has-text-centered">작성자</th>
        <th class="has-text-centered">작성일자</th>
        <th class="has-text-centered">추천</th>
        <th class="has-text-centered">조회수</th>
      </tr>
    </thead>
    <tbody>
      {#await slugList then slugBoard}
        {#each slugBoard["list"] as slug}
          <tr>
            <td
              ><a href="/board/qna/article/{slug.article_id}">{slug.title}</a
              ></td
            >
            <td>{slug.username}</td>
            <td>{slug.created}</td>
            <td>{slug.like}</td>
            <td>{slug.views}</td>
          </tr>
        {/each}
      {:catch error}
        <tr>
          <td colspan="5">{error.message}</td>
        </tr>
      {/await}
    </tbody>
    <tfoot>
      <tr>
        <td colspan="5" />
      </tr></tfoot
    >
  </table>
  {#await slugList then slugBoard}
    <nav class="pagination is-centered" aria-label="pagination">
      <ul class="pagination-list">
        {#each Array(Math.ceil(slugBoard["cnt"] / pageLimit)) as n, i}
          <li>
            <!-- svelte-ignore a11y-missing-attribute -->
            <a
              class="pagination-link"
              class:is-current={i + 1 === currentPage}
              sveltekit:prefetch
              on:click={() => (currentPage = i + 1)}>{i + 1}</a
            >
          </li>
        {/each}
      </ul>
    </nav>
  {:catch error}
    {error.message}
  {/await}

  <div class="container">
    <div class="field is-horizontal" style="float: right;">
      {#if isLogged}
        <a href="/board/qna/write/question" class="button is-primary">글쓰기</a>
      {/if}
      <div class="select">
        <select bind:value={currentLimit}>
          {#each pageLimits as pl}
            <option value={pl.value}>
              {pl.label}
            </option>
          {/each}
        </select>
      </div>
    </div>
    <br />
  </div>
  <br />
</div>
