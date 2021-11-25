import * as _ from "lodash";

const toCamel = (str: string) => {
  return str.replace(/([-_][a-z])/ig, ($1) => {
    return $1.toUpperCase()
      .replace('-', '')
      .replace('_', '');
  });
};

const isObject = function (obj: unknown) {
  return obj === Object(obj) && !Array.isArray(obj) && typeof obj !== 'function';
};

export function keysToCamel<T>(obj: Record<string, any>[]): T[];
export function keysToCamel<T>(obj: Record<string, any>): T;
export function keysToCamel<T>(obj: Record<string, any>): T | T[] {
  if (isObject(obj)) {
    const n: Record<string, any> = {};

    Object.keys(obj)
      .forEach((k) => {
        n[toCamel(k)] = keysToCamel(obj[k]);
      });

    return n as T;
  } else if (Array.isArray(obj)) {
    return (obj as Record<string, any>[])
      .map((i) => keysToCamel(i)) as T[];
  }

  return obj as T;
}


export function keysToSnake<T>(obj: unknown[]): T[];
export function keysToSnake<T>(obj: unknown): T;
export function keysToSnake<T>(obj: unknown): T | T[] {
  if (isObject(obj)) {
    const n: Record<string, unknown> = {};

    Object.keys(obj as Record<string, unknown>)
      .forEach((k) => {
        n[_.snakeCase(k)] = keysToSnake((obj as Record<string, unknown>)[k]);
      });

    return n as T;
  } else if (Array.isArray(obj)) {
    return (obj as Record<string, any>[])
      .map((i) => keysToSnake(i)) as T[];
  }

  return obj as T;
}
