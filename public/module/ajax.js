import urls from './urls.js';

// class Ajax {
//   async get(url) {
//       const response = await fetch(url, fetchParams);
//       const responseData = await response.json();

//       return {
//           status: response.status,
//           data: responseData
//       };
//   }
// }

// const ajax = new Ajax();
// export default ajax;

const APIurl = urls.url;
const ajaxDebug = true;

/**
 * Поддерживаемые методы: GET и POST
 * @typedef {Object} ajaxMethod
 * @property {string} post
 * @property {string} get
 */
 const ajaxMethods = {
  post: 'POST',
  get: 'GET',
};

/**
 * Поддерживаемые http-статусы ответа: 200, 400, 404
 * @typedef {Object} ajaxStatus
 * @property {number} ok
 * @property {number} notFound
 * @property {number} badRequest
 */
const ajaxStatuses = {
  ok: 200,
  notFound: 404,
  badRequest: 400,
  invalidSession: 424,
};

/**
 * Выполняет ajax-запрос на сервер. При успешном выполнении вызывает callback
 * @param {Object} requestParams
 * @property {ajaxMethod} [method = "GET"]
 * @property {Url} [url = '/']
 * @property {any} body
 * @return {Promise}
 */
function ajaxCall(requestParams) {
  const url = APIurl + (requestParams.url || '/');
  const fetchParams = {
    body: JSON.stringify(requestParams.body),
    mode: 'no-cors',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
    },
    method: requestParams.method,
  };

  if (ajaxDebug) {
    console.log('ajax request', {url}, ': ' + fetchParams);
  }

  let status = 0;
  return fetch(url, fetchParams)
      .then((response) => {
        if (ajaxDebug) {
          console.log('ajax get ')
          console.log(response);
        }
        status = response.status;
        return response.json();
      })
      .then((response) => {
        if (ajaxDebug) {
          console.log('ajax resolved ' + status + ': ');
          console.log(response);
        }
        return {
          status,
          response,
        };
      })
      .catch((error) => {
        console.warn(error);
      });
}

// Плагин для общения с API
const ajax = {
  AJAX_METHODS: ajaxMethods,
  STATUS: ajaxStatuses,
  get: (requestParams) => ajaxCall({method: ajaxMethods.get, ...requestParams}),
  post: (requestParams) => ajaxCall({method: ajaxMethods.post, ...requestParams}),
};

export default ajax;
